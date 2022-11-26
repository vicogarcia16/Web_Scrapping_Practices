import requests
from bs4 import BeautifulSoup

headers = {
     "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" \
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}


url = 'https://stackoverflow.com/questions'

respuesta = requests.get(url, headers=headers)
# *Parseo 
soup = BeautifulSoup(respuesta.text, "lxml")
contenedor_de_preguntas = soup.find(id="questions") # *Encontrar elemento por ID
# *Encontrar elementos por tag y por clase
lista_de_preguntas = contenedor_de_preguntas.find_all('div', class_="s-post-summary")
for pregunta in lista_de_preguntas:
    #! Metodo 1
    # *Dentro de cada elemento buscar por tag
    texto_pregunta = pregunta.find('h3').text
    descripcion_pregunta = pregunta.find(class_='s-post-summary--content-excerpt').text
    descripcion_pregunta = descripcion_pregunta.replace('\n', '').replace('\r', '') # *Limpiar datos
    print(texto_pregunta)
    print(descripcion_pregunta)
    print()
    
    #! Metodo 2
    contenedor_pregunta = pregunta.find('h3')
    texto_pregunta = contenedor_pregunta.text
    descripcion_pregunta = contenedor_pregunta.find_next_sibling('div')
    texto_descripcion_pregunta = descripcion_pregunta.text

    texto_descripcion_pregunta = texto_descripcion_pregunta.replace('\n', '').replace('\t', '')
    print(texto_pregunta)
    print(texto_descripcion_pregunta)
    print()
    
    

    

