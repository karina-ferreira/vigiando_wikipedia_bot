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
planilha_enviadas = planilha.worksheet("mensagens_enviadas") 
planilha_recebidas = planilha.worksheet("mensagens_recebidas")



def bibliotecas_variaveis():
  
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
  planilha_enviadas = planilha.worksheet("mensagens_enviadas") 
  planilha_recebidas = planilha.worksheet("mensagens_recebidas")
  
  return
