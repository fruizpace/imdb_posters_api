import requests
"direccion = http://www.omdbapi.com/?apikey=[yourkey]&  # [yourkey] = poner el código que nos han enviado al correo, cada vez que uses la API."

direccion = "http://www.omdbapi.com/?apikey=56568558&i=tt3896198" # url a la que quiero llamar

# Ejemplo de cómo hacer peticion HTTP
respuesta = requests.get(direccion)
if respuesta.status_code == 200: # los tipos de error en https://developer.mozilla.org/es/docs/Web/HTTP/Status
    print(respuesta.text)
    datos = respuesta.json() # Guardamos la info en formato json. Datos es un diccionario!
else:
    print("Se ha producido un error", respuesta.status_code)