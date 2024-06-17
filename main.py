from fastapi import FastAPI, Query
import requests 

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe uma mensagem incrivel do mundo da programação
    '''
    return {'Hello' : 'World'}


#http://localhost:8000/api/restaurantes?restaurante=McDonald%E2%80%99s
@app.get('/api/restaurantes')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes
    '''
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados':dados_json}

        #criando uma lista
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:   
                dados_restaurante.append({
                    "item": item['Item'],
                    "prece": item['price'],
                    "description": item['description']
                })
        
        return {'Restaurante':restaurante, 'Cardapio':dados_restaurante}


    else:
        return {'Erro':f'{response.status_code} - {response.text}'}

#rodar o projeto fastapi
#uvicorn main:app --reload

#porta http://localhost:8000/api/hello

#documentação
#http://localhost:8000/docs