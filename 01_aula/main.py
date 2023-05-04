import requests
import pandas as pd
import sys
import collections

url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotofácil'

r = requests.get(url)

r.text
r_text = r.text

df = pd.read_html(r_text)

type(df)
type(df[0])

df=df[0].copy()