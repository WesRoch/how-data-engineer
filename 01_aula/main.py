import requests
import pandas as pd
import sys
import collections

url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotofácil'

r = requests.get(url, verify=False)

r.text
#cleaning our dataframe
r_text = r.text.replace('\\r\\n', '')
r_text = r.text.replace('\r\n', '')
r_text = r.text.replace('"\r\n}', '')
r_text = r.text.replace('{\r\n "html": "', '')
r_text

df = pd.read_html(r_text, flavor='html5lib')

# returning our dataframe type
type(df)
type(df[0])

df=df[0].copy()