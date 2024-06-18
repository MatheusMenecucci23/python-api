# FastAPI Restaurante API

Este projeto é uma API simples construída com FastAPI para exibir cardápios de restaurantes. O projeto inclui endpoints para obter uma saudação simples e para recuperar cardápios de restaurantes específicos a partir de uma URL externa.

## Funcionalidades

- **Hello World Endpoint:** Exibe uma mensagem de saudação simples.
- **Restaurantes Endpoint:** Recupera cardápios de restaurantes específicos a partir de uma URL externa.

## Estrutura do Projeto

- `main.py`: Contém a definição dos endpoints e a lógica principal da aplicação.
- `requirements.txt`: Lista de dependências do projeto.
- `README.md`: Instruções e informações sobre o projeto.

## Endpoints

### /api/hello

Este endpoint retorna uma mensagem de saudação simples.

**Exemplo de Requisição:**
  ```bash
  GET [/api/hello](http://localhost:8000/api/hello)
   ```

# API de Restaurantes

Este endpoint recupera os cardápios dos restaurantes a partir de uma URL externa. Pode ser usado para listar todos os restaurantes ou filtrar por um restaurante específico.

## Parâmetros de Query

- `restaurante` (opcional): Nome do restaurante para filtrar os resultados.

## Exemplo de Requisição

```bash
GET /api/restaurantes?restaurante=McDonald’s
 ```
## Instruções de Uso

### Instalação

1. Clone o repositório.
   
   ```bash
   git clone <url-do-repositório>
   ```
2. Crie um ambiente virtual e ative-o:
   
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3. Instale as dependências:
   
    ```bash
    pip install -r requirements.txt
    ```
     
## Executando a Aplicação

Para iniciar o servidor FastAPI, execute o seguinte comando:

  ```bash
  uvicorn main:app --reload
  ```
## Documentação

A documentação interativa da API está disponível em [http://localhost:8000/docs](http://localhost:8000/docs).

## Script de Exportação de Dados

O script em `main.py` também inclui um exemplo de como consumir a URL externa para obter dados de restaurantes, processá-los e salvá-los em arquivos JSON separados para cada restaurante.

### Exemplo de Execução do Script:

1. Acesse a URL externa e obtenha os dados dos restaurantes.
2. Organize os dados em um dicionário onde a chave é o nome do restaurante.
3. Salve os dados em arquivos JSON separados para cada restaurante.
 ```bash
import requests
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()

    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "prece": item['price'],
            "description": item['description']
        })

    for nome_do_restaurante, dados in dados_restaurante.items():
        nome_do_arquivo = f'{nome_do_restaurante}.json'
        with open(nome_do_arquivo, 'w') as arquivo_resturante:
            json.dump(dados, arquivo_resturante, indent=4)

else:
    print(f'O erro foi {response.status_code}')


