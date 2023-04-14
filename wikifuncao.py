import datetime
import pandas as pd
import requests
import json

from io import StringIO 

def wikifuncao(verbete):

  BASE_URL = "http://pt.wikipedia.org/w/api.php" 

  parameters = { 'action': 'query',
            'format': 'json',
            'continue': '',
            'titles': verbete,
            'prop': 'revisions',
            'rvprop': 'content|size|ids|timestamp|sha1|comment|flags|user|userid',
            'rvlimit': 'max',  
            'rvdir': 'older'}

  wp_call = requests.get(BASE_URL, params=parameters)
  response = wp_call.json()

  title = parameters['titles'].replace('_',' ')

  total_revisions = 0
  revisoes = []

  while True:
    wp_call = requests.get(BASE_URL, params=parameters)
    response = wp_call.json()

    try: 
      for page_id in response['query']['pages']:  
        total_revisions += len(response['query']['pages'][page_id]['revisions'])
        revisoes += response['query']['pages'][page_id]['revisions']
    except:
      resposta = "Esse verbete não existe, ou você digitou errado. Confira e tente outra vez!"
      return resposta

    if 'continue' in response:
      parameters['continue'] = response['continue']['continue']
      parameters['rvcontinue'] = response['continue']['rvcontinue']
    

    else:
      break

  print (total_revisions)
  rev_json = json.dumps(revisoes) 
  df_revisoes = pd.read_json(StringIO(rev_json))

  data_primeira = df_revisoes.iloc[-1]["timestamp"]
  data_primeira = data_primeira.date().strftime('%d/%m/%Y')

  df_revisoes.columns

  df_revisoes.head()
  df_revisoes['timestamp'] = pd.to_datetime(df_revisoes['timestamp']) 
  df_revisoes = df_revisoes.sort_values("timestamp", ascending=False) 

  first= df_revisoes["*"].loc[1]
  df_revisoes['*'] = df_revisoes['*'].astype(str)
  df_revisoes['tamanho'] = df_revisoes['*'].apply(lambda x: len(x))
  df_revisoes['tamanho_anterior'] = df_revisoes['tamanho'].shift(-1)
  df_revisoes['tamanho_edicao'] = df_revisoes['tamanho'] - df_revisoes['tamanho_anterior']

  df_30_dias = df_revisoes[df_revisoes.timestamp.dt.date > pd.to_datetime(datetime.datetime.now() - pd.to_timedelta("30day"))]
  df_30_60_dias = df_revisoes[(df_revisoes.timestamp.dt.date > pd.to_datetime(datetime.datetime.now() - pd.to_timedelta("60day"))) & (df_revisoes.timestamp.dt.date < pd.to_datetime(datetime.datetime.now() - pd.to_timedelta("30day")))] 

#________________________________[análises]__________________________________#

  vezes_editado = df_30_dias.shape[0]

  if df_30_dias.shape[0] == 0:
      print(f'Não houve alterações no verbete.')

  else:
      print(f'Foi editado {vezes_editado}.')

  df_30_60_dias['tamanho_edicao'].sum()
  diferenca =  df_30_dias['tamanho_edicao'].sum() - df_30_60_dias['tamanho_edicao'].sum()

  um_mes = df_30_dias['tamanho_edicao'].sum()

  dois_meses = df_30_60_dias['tamanho_edicao'].sum()

  if dois_meses == 0:
      R = 0
      print(f'No mês anterior a este, o verbete {title} não foi editado.')
      
  else:
      R = round((diferenca/ dois_meses) * 100)

      if R > 0:
          print(f'A edição aumentou {R}% em tamanho, em comparação aos 30 dias anteriores.') 
      elif R <0:
          print(f'A edição diminuiu {R}% em tamanho, em comparação aos 30 dias anteriores.')
      else:
          print(f'A edição não mudou de tamanho, em comparação aos 30 dias anteriores.') 

  usuario_editor = df_30_dias['user'].unique()
  num = len(usuario_editor)
  if num > 0:
      print(f'Esse verbete foi editado por {num} usuários.')
  else:
      print(f' ') 

  df_usuarios = df_30_dias['user'].value_counts().to_frame()
  print(df_usuarios.shape)
  df_usuarios = df_usuarios.reset_index().rename(columns={'index':'usuario', 'user':'#edicoes'})

  if df_usuarios.shape[0]==0:
      print(f'Esse verbete não foi editado nos últimos 30 dias.')
  else:
      usuario =  df_usuarios.loc[0]['usuario']
      n_edicoes = df_usuarios.loc[0]['#edicoes']
      print(f'Quem mais editou este verbete foi {usuario}, com {n_edicoes} edições.') 


#________________________________[resultados]__________________________________#

  resposta = f'Nos últimos 30 dias, o verbete {title}:'

  if df_30_dias.shape[0] == 0:
      resposta = resposta +  f'\nNão sofreu alterações.'
  else:
      resposta = resposta + f'\nFoi editado {vezes_editado} vezes.'

  if num > 1:
      resposta = resposta +  f'\nFoi editado por {num} usuários.'

  elif num == 1:
      resposta = resposta + f'\nFoi editado por {num} usuário(s).'
  else:
      resposta = resposta + f' '

  if df_usuarios.shape[0]==0:
      resposta = resposta + f' '
      
  else:
      usuario =  df_usuarios.loc[0]['usuario']
      n_edicoes = df_usuarios.loc[0]['#edicoes']
      resposta = resposta + f'\nQuem mais editou este verbete foi {usuario}, com {n_edicoes} edições.'

  if R > 0:
      resposta = resposta + f'\nO tamanho da edição aumentou {R}%, em comparação aos 30 dias anteriores.'
  elif R <0:
      resposta = resposta + f'\nO tamanho da edição diminuiu {R}%, em comparação aos 30 dias anteriores.'
  else:
      resposta = resposta + f'\nNo período de 30 dias anterior a este, o verbete {title} não foi editado.'

  resposta = resposta + f' \nDesde sua criação, em {data_primeira}, o verbete {title} foi editado {total_revisions} vezes.'
  return resposta
