import requests

API_KEY =  56568558
url_template = "http://www.omdbapi.com/?apikey={}&{}={}"

class PeticionError(Exception): # clase que hereda de Excpetion
    pass

def peticion(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200: # si ha ido bien...
        datos = respuesta.json() # guarda la respuesta
        if datos['Response'] == "False": # si la respuesta tiene resultado negativo
            raise Exception(datos['Error'])
        else: # si la respuesta tiene resultado positivo (o sea hay info de pelis)
            return datos
    else:
        raise Exception("Error de consulta: {}".format(respuesta.status_code))

iniciador = 'y'
while iniciador == 'y':
    try:
        pregunta = input('Título de la película: ')
        respuesta = peticion(url_template.format(API_KEY,'s', pregunta)) # 's' = search
        primera_peli = respuesta['Search'][0] # 1er elemento de la lista de pelis que coinciden con el título
        clave = primera_peli['imdbID'] # identificador de la primera peli

        respuesta = peticion(url_template.format(API_KEY, 'i', clave))
        titulo = respuesta['Title']
        agno = respuesta['Year']
        director = respuesta['Director']
        print("La película {} ({}) fue dirigida por {}.".format(titulo, agno, director))
        
    except Exception as e: # metemos en "e" el error y luego lo imprimo
        print(e)
        
    iniciador = input('¿Quieres buscar otra película? (y/n): ').lower()