#%%
# import requests
import requests
import json

#%%
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'

ret = requests.get(url)

#%%

print(ret) # response 200 - success

# %%

print(ret.text)
# %%

url_erro = 'https://economia.awesomeapi.com.br/json/wrr/USD-BRL'

ret_erro = requests.get(url_erro)
# %%

if ret_erro:
    print(ret_erro) ## caso a request fosse certa, retornaria a variavel com a response 200
else:
    print('Falhou,', ret_erro) ## irá retornar 404, requisição aonde n existe
# %%

dolar = json.loads(ret.text)['USDBRL']
# %%

print( f"20 Dólares hoje custam {float(dolar['bid']) * 20} reais")
# %%