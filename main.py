import requests

# Buscar una película por el título
pregunta = input('Título de la película: ')
API_KEY =  56568558
# construimos la direccion para solicitar la info de la peli
direccion = "http://www.omdbapi.com/?apikey={}&s={}".format(API_KEY, pregunta)

respuesta = requests.get(direccion)

if respuesta.status_code == 200: 
    datos = respuesta.json() # Datos es un diccionario!
    if datos['Response'] == "False":
        print(datos["Error"])
    else:
        primera_peli = datos['Search'][0] # 1er elemento de la lista de pelis que coinciden con el título
        clave = primera_peli['imdbID'] # identificador de la primera peli
        
        otra_direccion = "http://www.omdbapi.com/?apikey={}&i={}".format(API_KEY, clave)
        nueva_respuesta = requests.get(otra_direccion)
        if nueva_respuesta.status_code == 200:
            datos = nueva_respuesta.json()
            if datos['Response'] == "False":
                print(datos["Error"])
            else:
                titulo = datos['Title']
                agno = datos['Year']
                director = datos['Director']
                print("La peli {}, del año {}, fue dirigida por {}").format(titulo, agno, director)
        else:
            print('Error en consulta por id:', nueva_respuesta.status_code)
else:
    print("Error en búisqueda", respuesta.status_code)