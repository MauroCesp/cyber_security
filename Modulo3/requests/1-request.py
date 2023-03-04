
# Este es el modulo standard de python para realizar peticiones
# Facilita las cosas para enviar peticiones
# NO hay necesidad de codificar los datos post

import requests

# dir(request) ---- Para ver los modulos disponibles

# Y simplemente pedimos la coneccion
responseGet = requests.get("https://www.wikipedia.com")

print(responseGet)

print(dir(responseGet))

print(responseGet.status_code)

# Esto nos devuelve el HTML 
print(responseGet.text)

# Devuelve un diccionario clave valor con las cabeceras que lo puedo recorrer.
print(responseGet.headers)


# Tambien se puede hacer una peticion POST
responsePost = requests.post("http://www.google.com")
# 405 es que enviamos una peticion y no estaba autorizada POST
print(responsePost.status_code)
print(responsePost.headers)
print(responsePost.text)