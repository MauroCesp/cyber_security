import http.client

# Ahora intento realizar una conexion/una peticion
# Primero necesito establecer una conneccion para despues realizar la peticion

connection = http.client.HTTPConnection("www.google.com")
headers= {}
params= {}

# aqui ya realizamos la coneccion
connection.request("GET", "", params, headers)

# Despues lo metemos en un objeto RESPONSE

response = connection.getresponse()

# Ahora cojo la funcion e imprimo su contenido para ver los distitos atributos y los metodos que podemos utilizar.
print(dir(response))

# Auqi nos interesan varias cosas
# El resultado es que Google nos redirecciona al CAPTCHA para comprobar si soms un ronot 
# Ahi formas de hacer un bypass al captch
# Redirecciones son codigos 300
# LOCATION es el atributo es el que nos dice donde nos tenemos que redirigir.
print(response.status)

print(response.headers)

print(response.info)
print(response.read())