#%%
from bs4 import BeautifulSoup as bs
import requests
import logging
import pandas as pd
# %%

url = 'https://portalcafebrasil.com.br/todos/podcasts/'
# %%

ret = requests.get(url)
# %%

ret.text # mostrando nossa url em text
# %%

soup = bs(ret.text)
# %%

print(soup)
# %%

soup.find('h5') # procurando o elemento h5 (header 5 - html)
# %%

soup.find('h5').text #type: ignore
# %%
soup.find('h5').a # type: ignore | elemento a (link do podcast)
# %%

soup.find('h5').a['href'] # type: ignore

# %%

lst_podcast = soup.find_all('h5') # colocando todos os h5 em uma list
# %%

for item in lst_podcast:
    print(f"EP: {item.text} - Link: {item.a['href']}") # limitado a 16 ep/link por pagina
# %%

url = 'https://portalcafebrasil.com.br/todos/podcasts/page/{}/?ajax=true'
# %%

url.format(5)
# %%

def get_podcast(url):
    ret = requests.get(url)
    soup = bs(ret.text)
    return soup.find_all('h5')

# %%

get_podcast(url.format(5))

#%%

log = logging.getLogger()
log.setLevel(logging.DEBUG)
# que informações vamos apresentar
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
ch = logging.StreamHandler() 
ch.setFormatter(formatter) 
log.addHandler(ch) 
# %%

i = 1
lst_podcast = []
lst_get = get_podcast(url.format(i))
log.debug(f"Coletado {len(lst_get)} episódios do link: {url.format(i)}")
while len(lst_get ) > 0:
    lst_podcast =lst_podcast + lst_get
    i += 1
    lst_get = get_podcast(url.format(i))
    log.debug(f"Coletado {len(lst_get)} episódios do link: {url.format(i)}")
# %%

len(lst_podcast) # qtd de episódios no total
# %%

lst_podcast
# %%

df_podcast = pd.DataFrame(columns=['nome', 'link']) # formato do df 
# %%

for item in lst_podcast:
    df_podcast.loc[df_podcast.shape[0]] = [item.text, item.a['href']] # type: ignore
# %%
df_podcast.shape
# %%
df_podcast
# %%

df_podcast.to_csv('banco_de_podcast.csv', sep=';', index=False) # separador e Sem index