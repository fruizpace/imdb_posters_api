import requests

API_KEY =  56568558
url_template = "http://www.omdbapi.com/?apikey={}&{}={}"

def peticion(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200: # si ha ido bien...
        datos = respuesta.json() # guarda la respuesta
        if datos['Response'] == "False": # si la respuesta tiene resultado negativo
            return datos["Error"] # string
        else: # si la respuesta tiene resultado positivo (o sea hay info de pelis)
            return datos
    else:
        return respuesta.status_code #string

pregunta = input('Título de la película: ')

# Petición 1: para obtener identificador de la peli
respuesta = peticion(url_template.format(API_KEY,'s', pregunta)) # 's' = search
if isinstance(respuesta, str):
    print("Error en consulta: ", respuesta)
else: # si da un diccionario
    primera_peli = respuesta['Search'][0] # 1er elemento de la lista de pelis que coinciden con el título
    clave = primera_peli['imdbID'] # identificador de la primera peli
    # Petición 2: con el id ahora puedo acceder a más info de la peli
    respuesta = peticion(url_template.format(API_KEY, 'i', clave))
    if isinstance(respuesta, str):
        print(respuesta)
    else:
        titulo = respuesta['Title']
        agno = respuesta['Year']
        director = respuesta['Director']
        print("La película {} ({}) fue dirigida por {}.".format(titulo, agno, director))