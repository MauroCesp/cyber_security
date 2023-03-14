# Lo primero que se hace es un update a Kali
# Despues se installa Docker ------> apt install -y docker.io

# Ahora se añade  el usuario al grupo de docker utilizando este comando ---> usermod -aG docker $USER
# docker run *------> Para llamar a un contenedor a traves del cual levantamos una aplicacion
# EL contenedor va a tener el aplicativo web vulnerable


# https://hub.docker.com/r/vulnerables/web-dvwa

# -rm  -----> se le indica a docker que borre el contenedor cuando se mate el proceso
# -i -----> Interactivo 
# t ----> se abre una shell. Entonces se abre una shell interactiva para enviar comandos TTY
# El trafico de red de el docker va a llegar al puerto 80
# Despues se hace referencia a la ruta dentro de hub de docker
# Se usa el puerto 8083 para ver donde esta

#docker run --rm -it -p 8083:80 vulnerables/web-dvwa

# docker ps -------> se ve la imagen que se acaba de levantar y el redireccionamiento de puertos

#-------------------------------------------
# Cuando se levanta el aplicativo, tambien se levanta una red llamada docker0
# Es la que se utiliza
# Es necesario ir a localhost:8083 para ver el aplicativo y terminarlo de configurar ahi con security LOW

# Se le da en create/reset database ----> la primera vez

#--------------------------------------------


# Ahora se necesita levantar un Wireshark
# En la consola se corre el comando -------> wireshark 

# En la consola de Wireshark NO se monitoriza la interfaz eth0
# Se lee la red virtual docker0

# COn un overmouse sobre la red se observa la IP

# Con la session abierta de wireshark es necesario ingresar al aplicativo web
# Se analizan los resultados desde wireshark
# Realmente lo que interesa es el HTML/HTP donde estan lo banners.
# Si nos logeamos vemos en wireshark que se pruduce un triple hand shake y despues una peticion a un archivo php (login.php)

# Se interactua con este login, y se obtienen sus cookies de session
# Y despues se pueden explotar vulneranilidades de forma programatica

# La cookie de session es un dato importante porque si no se tiene la cookie no se puede interactuar.
# con la libreria REQUEST 
# 


# ---------------- IMPORTO MODULOS ----------------

# Beatiful soup lo que hace es ayudar a buscar informacion de una manera mas limpia
# Lo que se hara es eliminar todo el HTML y guardar solo el contenido que buscamos.
# Se pueden alterar el texto de las etiquetas HTML , guardar titulos , numero de enlaces.

import requests

# Se instala de la siguiete manera:
# python -m pip install beatifulsoup4

# Esta es la forma en que se importa
from bs4 import BeautifulSoup 



# Se tratara de encontrar el USER_TOKEN
# Se crea  una funcion y se le pasa un Source
# Con esta informacion esta claro que se hara una sopa de beatifulsoup
def get_token(source):
    # Se le indica a la libreria de Beatifulsoup el contenido y el parser que se dedsea utilizar. Esa es la sopa
    # Esta libreria depende de un parser, el mas utilizado es LXML porque soporta varios formatos
    # Se puede probar html.parser
    soup = BeautifulSoup(source, "html.parser") 
    # Para el token se busca un input de tipo hidden y se quiere obtener su valor.
    return soup.find('input',{'type':'hidden'})['value']


# Se necesita hacer una peticion a la URL
# Donde esta -----> Es el aplicativo web que intalamos en docker.
url = 'http://localhost:8083/login.php' 


#-------- REQUEST object
# Se crea un objeto que sea una session
# Esto se hace  para evitar que cada vez que se envie un reuqest se obtenga el token ID
# Esto crea un objeto de session que se utiliza para establacer coneccion
# Se llamara S
with requests.Session() as s:
    # Simplemente se saca la respuesta y de esa respuesta se hace un print
    src  = s.get(url).text
    
    # Dentro del codigo HTML estara la inforamcion del usuario y las cookies de session
    # Lo mismo que se ha visto desde Wireshark
    #print(source)
    token = get_token(src)

    # Cada vez que se hace una peticion cambia el token
    print(token)

    # -------- USER -PSW ---------------
    # Ahora se envia un diccionario (clave,valor) con la information del formulario

    # Se puede revisar en wireshark, donde tenemos los elementos fundamentales para realizar la peticion de tipo post.
    creds = {
        'username':'admin',
        'password':'password',
        'Login':'Login',
        # Como recojemos el token con nuestra funcion , le pasamos el source
        'user_token':token

    }

    # Ahora para realizar una peticion post se utiliza la session a la URL con los datos que se le ingresan a continuacion.
    response = s.post(url,data = creds)

    print(response.text)