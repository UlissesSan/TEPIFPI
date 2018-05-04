
Tópicos Especiais em Programação

Exercício 1 -  Demonstração de uso de APIs


1) Nome da API

	The Movie DB.


2) Utilidade

	Coleta de dados sobre filmes e Fazer listas de filmes.


3) Link ou endpoint

	https://api.themoviedb.org/3/account/" + user_id + "/lists?page=1&session_id=" + session_id + "&language=en-US&api_key=" + key
    


4) Possíveis recursos. 

	Classificar filmes e criar listas.


5) Métodos suportados

	DELETE, POST, GET

6) Exemplo(s) GET

     list_movies()

7) Exemplo(s) POST

     add_movie_to_list(‘list_id’, ‘movie_id’)
