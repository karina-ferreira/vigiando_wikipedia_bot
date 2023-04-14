import os

import gspread
import json
import pandas
import requests
import time

from datetime import date, time
from datetime import datetime
from flask import Flask, request
from io import StringIO 
from oauth2client.service_account import ServiceAccountCredentials

import gravar_sheets
import wikifuncao

# ______________________________[variáveis de ambiente]_________________________

TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]
GOOGLE_SHEETS_KEY = os.environ["GOOGLE_SHEETS_KEY"]
GOOGLE_SHEETS_CREDENTIALS = os.environ["GOOGLE_SHEETS_CREDENTIALS"] 
with open("credenciais.json", mode="w") as arquivo:
  arquivo.write(GOOGLE_SHEETS_CREDENTIALS)
  
conta = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json")
api = gspread.authorize(conta)
planilha = api.open_by_key(f'{GOOGLE_SHEETS_KEY}')
planilha_enviadas = planilha.worksheet("mensagens_enviadas") 
planilha_recebidas = planilha.worksheet("mensagens_recebidas")
  
# ______________________________[site]__________________________________________

app = Flask(__name__)

@app.route("/")
def index():
  return "Esse é o site de teste"

# ______________________________ bot (FUNCIONANDO) _____________________________

 
# Variável global para armazenar o update_id da última mensagem processada
last_update_id = 0

@app.route("/telegram-bot", methods = ["POST"])
def telegram_bot():
    global last_update_id

    update = request.json 

    # Verifica se há uma nova mensagem a ser processada
    if update["update_id"] > last_update_id:
        last_update_id = update["update_id"]

        # Dados da mensagem
        first_name = update['message']['from']['first_name']
        last_name = update['message']['from']['last_name']
        user_name = update['message']['from']['username']
        sender_id = update['message']['from']['id']
        chat_id = update['message']['chat']['id']
        message = update["message"]["text"]
        date = datetime.fromtimestamp(update['message']['date']).date()
        time = datetime.fromtimestamp(update['message']['date']).time()

        resposta_wiki = wikifuncao.wikifuncao(message)
        
        # Define resposta
        if message == "/start":
            texto_resposta = f'\nBoas vindas! Eu sou o bot da <b>Vigiando a Wikipédia</b>, uma ferramenta que permite acompanhar como, quando e por quem a história está sendo narrada, alterada ou eliminada.\n\n  Você escolhe um verbete da Wikipédia, e eu faço algumas análises sobre ele. Na próxima mensagem, envie o verbete que você deseja acompanhar.\n\n Lembre-se: ele precisa estar escrito tal qual aparece no site da Wikipédia, com cada inicial maiúscula e separado por espaços (exemplo: Oceano Atlântico)\n\nVamos lá!\n\n <i> Envie o verbete escolhido na próxima mensagem. A depender de quão volumoso ele é em tamanho e versões editadas, a consulta pode demorar alguns minutos.</i>"
        else:
            texto_resposta = resposta_wiki 
            
        # Envia a resposta        
        nova_mensagem = {"chat_id": chat_id, "text": texto_resposta, "parse_mode": 'html'} 
        requests.post(f"https://api.telegram.org./bot{TELEGRAM_API_KEY}/sendMessage", data=nova_mensagem)

        # Atualiza planilha do sheets com último update processado
        #gravar_sheets.gravar_sheets(nova_mensagem)

    return "ok"
