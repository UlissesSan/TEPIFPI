"""
API do The Movie DB

1) Nome da API
	The Movie DB

2) Utilidade
	Coleta de dados sobre filmes

3) Link ou endpoint
	https://api.themoviedb.org

4) Possiveis recursos. 
	Dados sobre filmes

5) Metodos suportados
	#Delete List
	#Add Movie
	#Get Details

6) Exemplo(s) em python do metodo get
7) Exemplo(s) em python do petodo post
"""

import requests

key = ''
request_token = ""
access_token = ''
session_id = ''

user_id = '7875054'

# dominio da api
domain = 'https://api.themoviedb.org'


def list_movies():
    #Mostra a lista de filmes criada por um usuario.#
    # url a ser montada para acessar o servico a ser requisitado
    url = domain + "/3/account/" + user_id + "/lists?page=1&session_id=" + session_id + "&language=en-US&api_key=" + key
    response = requests.get(url).json()

    return response


def add_movie_to_list(list_id, movie_id):
    #Adiciona um titulo a uma lista de filmes de um usuario#
    # url a ser montada para acessar o servico a ser requisitado
    url = domain + "/3/list/" + list_id + "/add_item?session_id=" + session_id + "&api_key=" + key
    # item a ser adicionado ao metodo post
    payload = "{\"media_id\":%s}" % movie_id

    headers = {'content-type': 'application/json;charset=utf-8'}
    response = requests.post(url, data=payload, headers=headers)

    return response


# mostra o resustado da funcao na Tela (id da lsita que criei)
#print(add_movie_to_list('64695', '591'))


# chama o resultado da funcao List_movies na tela
print(list_movies())

