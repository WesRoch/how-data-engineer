#%%
# import requests
import requests
import json
import backoff
import random

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
    print('Falhou,', ret_erro) ## irá retornar 404, req n existe
# %%

dolar = json.loads(ret.text)['USDBRL']
# %%

print( f"20 Dólares hoje custam {float(dolar['bid']) * 20} reais")
# %%

def cotacao(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}' # melhor forma(no caso)
    # url = 'https://www.economia.awesomeapi.com.br/json/last{}'.format(moeda) -> outra forma de concatenar
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-', '')]
    print(
        f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor } {moeda[-3:]}"
    )
# %%

cotacao(20,'USD-BRL')
# %%

cotacao(100, 'AUD-BRL')
    
# %%
# tratando um erro quando passa um paramatro diferente na funcao

try:
    cotacao(20, 'Wrr')
except:
    pass


# %%
## tratando o erro e retornando a mensagem do erro com o Exception
try:
    cotacao(50, 'wrrr')
except Exception as e:
    print(e)
else:
    print("ok")
# %%

def multi_moedas(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-', '')]
    print(
        f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor } {moeda[-3:]}"
    ) 
# %%

multi_moedas(30, 'ARS-BRL')
# %%
# como tratar de um erro sem o try except?

def error_check(func): # passando func como atributo da funcao
    def inner_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print(f"{func.__name__} falhou")
    return inner_func

@error_check
def multi_moeda(valor, moeda): # para essa funcao executar, irá passar pelo error check
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-', '')]
    print(
        f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor } {moeda[-3:]}"
    ) 

# %%
multi_moeda(30, 'ARS-BRL')
multi_moeda(30, 'USD-BRL')
multi_moeda(30, 'AUS-BRL')
multi_moeda(30, 'JPY-BRL')
multi_moeda(30, 'EUR-BRL')

# %%
# usando a library backoff

@backoff.on_exception(backoff.expo,(ConnectionAbortedError, ConnectionRefusedError, TimeoutError))
def test_func(*args, **kargs):
    rnd = random.random()
    print(f"""
          RND: {rnd}
          args: {args if args else 'sem args'}
          kargs: {kargs if kargs else 'sem kargs'} 
          """)
    if rnd < .2: # refazendo as tentativas e retornando os erros
        raise ConnectionAbortedError("Conexão foi finalizada")
    elif rnd < .4:
        raise ConnectionRefusedError("Conexao foi recusada.")
    elif rnd < .6:
        raise TimeoutError("Tempo de espera excedido.")
    else:
        return "OK!"

# %%
test_func()
# %%
test_func(30)
# %%
test_func(30, 24, nome='wesley')
# %%
