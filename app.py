#importando o modulo todo
import requests
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url)

print(response)

if response.status_code == 200:
    dados_json = response.json()
    #print(dados_json)

    #criando um dicionario
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        #se o restaurante não estiver nos dados
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "prece": item['price'],
            "description": item['description']
        })

else: 
    print(f'O erro foi {response.status_code}')

#arquivos
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo,'w') as arquivo_resturante:
        json.dump(dados, arquivo_resturante, indent=4)