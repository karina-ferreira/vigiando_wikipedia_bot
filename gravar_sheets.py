import os
import gspread
import json

from oauth2client.service_account import ServiceAccountCredentials

# ______________________________[variáveis de ambiente]_________________________

GOOGLE_SHEETS_KEY = os.environ["GOOGLE_SHEETS_KEY"]
GOOGLE_SHEETS_CREDENTIALS = os.environ["GOOGLE_SHEETS_CREDENTIALS"] 
with open("credenciais.json", mode="w") as arquivo:
  arquivo.write(GOOGLE_SHEETS_CREDENTIALS)
conta = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json")
api = gspread.authorize(conta)
planilha = api.open_by_key(f'{GOOGLE_SHEETS_KEY}')
planilha_enviadas = planilha.worksheet("mensagens_enviadas") 
planilha_recebidas = planilha.worksheet("mensagens_recebidas")

# ______________________________[função]_________________________

def gravar_sheets():
  
    recebidas = []
    for mensagem in mensagens:
        if mensagem[1] == "recebida":
            recebidas.append(mensagem)
            planilha_recebidas.append_rows(recebidas)

    enviadas = []
    for mensagem in mensagens:
        if mensagem[1] == "enviada":
            enviadas.append(mensagem)
            planilha_enviadas.append_rows(enviadas)
    
    return 
