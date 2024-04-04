import requests
 
movie = input("Digite o título do filme: ")
 
url = f'https://www.omdbapi.com/?apikey=436d40d9&t={movie}'
  
response = requests.get(url, verify=False)   
data = response.json()
 
 
if response.status_code == 200:
     print("Título:", data['Title'])
     print("Ano:", data['Year'])
     print("IMDB:", data['imdbRating'])
     print("Diretor:", data['Director'])
     print("Atores:", data['Actors'])
     print("Enredo:", data['Plot'])
else:
    print("Erro ao obter informações do filme.")