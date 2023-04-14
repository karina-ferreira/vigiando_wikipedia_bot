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

import WikiFuncao

# ______________________________[variáveis de ambiente]_________________________

TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]
GOOGLE_SHEETS_KEY = os.environ["GOOGLE_SHEETS_KEY"]
GOOGLE_SHEETS_CREDENTIALS = os.environ["GOOGLE_SHEETS_CREDENTIALS"] 
with open("credenciais.json", mode="w") as arquivo:
  arquivo.write(GOOGLE_SHEETS_CREDENTIALS)
  
conta = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json")
api = gspread.authorize(conta)
planilha = api.open_by_key(f'{GOOGLE_SHEETS_KEY}')
sheet_recebidas = planilha.worksheet("enviadas") 
sheet_mailing = planilha.worksheet("recebidas")
  
# ______________________________[site]__________________________________________

app = Flask(__name__)

@app.route("/")
def index():
  return "Esse é o site do Vigiando Wikipédia Bot"

# ______________________________[bot do telegram]_____________________________

@app.route("/telegram-bot", methods = ["POST"])
def telegram_bot():
  
    update = request.json 

# Dados da mensagem
    update_id = update['update_id']
    first_name = update['message']['from']['first_name']
    last_name = update['message']['from']['last_name']
    user_name = update['message']['from']['username']
    sender_id = update['message']['from']['id']
    chat_id = update['message']['chat']['id']
    message = update["message"]["text"]
    date = datetime.fromtimestamp(update['message']['date']).date()
    time = datetime.fromtimestamp(update['message']['date']).time()

# Define resposta

    if message == "/start":
        texto_resposta = "Olá! Seja bem-vinda(o). Esse bot te dá algumas análises sobre a página da Wikipédia que você escolher. Na próxima mensagem, envie o título da página (verbete) que deseja acompanhar:"
    else:
        texto_resposta = WikiFuncao(message)
    nova_mensagem = {"chat_id": chat_id, "text": texto_resposta}
    requests.post(f"https://api.telegram.org./bot{token}/sendMessage", data=nova_mensagem)
    mensagens.append([datahora, "enviada", username, first_name, chat_id, texto_resposta])
        

# Atualiza planilha do sheets com último update processado

    recebidas = []
    for mensagem in mensagens:
        if mensagem[1] == "recebida":
            recebidas.append(mensagem)

    planilha_recebidas = planilha.worksheet("Mensagens Recebidas")
    planilha_recebidas.append_rows(recebidas)

    enviadas = []
    for mensagem in mensagens:
        if mensagem[1] == "enviada":
            enviadas.append(mensagem)

    planilha_recebidas = planilha.worksheet("Mensagens Enviadas")
    planilha_recebidas.append_rows(enviadas)
    
    
# Envia a resposta 

    nova_mensagem = {"chat_id": chat_id, "text": texto_resposta} 
    requests.post(f"https://api.telegram.org./bot{TELEGRAM_API_KEY}/sendMessage", data=nova_mensagem)

    return "ok"
