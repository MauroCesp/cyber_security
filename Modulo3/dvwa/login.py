# Lo primero que hago es hacerle un update a Kali
# Despues instalo ------> apt install -y docker.io

# Ahora a;adimos el usuario al grupo de docker utilizando este comando ---> usermod -aG docker $USER
# docker run *------> Para llamar a un contenedora traves del cual levantamos una aplicacion
# EL contenedor va a tener el aplicativo web vulnerable


# https://hub.docker.com/r/vulnerables/web-dvwa

# -rm  -----> le decimos a ocker que borre el contenedor cuando matemos el proceso
# -i -----> INteractivo 
# t ----> abre una shell. ENtonces abre una shel interactiva para enviar comandos TTY
# El trafico de red de el docker va a llegar al puerto 80
# Despues hacermos referencia a la ruta dentro de hub de docker
# VOy a usar el puerto 8083 para ver donde esta

#docker run --rm -it -p 8083:80 vulnerables/web-dvwa

# docker ps -------> podemos ver la imagen que acabamos levantar y vemos el redireccionamiento de puertos

#-------------------------------------------
# CUnado levantamos nueestro aplicativo se levanto una red llamada docker0
# Es la que vamos a utilizar
# Nos vamos a localhost:8083 para ver el aplicativo y lo terminamos de configurar ahi con security LOW

# Le damos en create/reset database ----> eso la primera vez

#--------------------------------------------


# Ahora necesito levantar un Wireshark
# En la consola corro el comando -------> wireshark 

# NO vamos a monitorizar la interfaz eth0
# Vamos a leer la red virtual docker0

# SI hacemos overmouse sobre la red podemos var la IP

# Con la session abierta de wireshark nos logeamos al aplicativo web
# Analizamos los resultados desde wireshark
# Realmente lo que nos interesa en el HTML/HTP donde estan lo banners.
# Si nos logeamos vemos en wireshar que se pruduce un triple hand shake y despues una peticion a un archivo php (login.php)
# COn lo que ya sabemos de web scrapping
# Vamos a interactuar ocn este login, quedarnos con sus cookies de session
# Y despues se pueden explotar vulneranilidad es de forma programatica

# La cookie de session es un dato importante porque si no tenemos la cookie no nos dejan interactuar.
# con la libreria REQUEST podemos interactuar con las cookies
# 


# ---------------- IMPORTO MODULOS ----------------

# Beatiful soup lo que hace es ayudar a buscar informacion de una manera mas limpia
# Lo que hacemos es eliminar todo el HTML y guardar el contenido.
# Se pueden alterar el texto de las etiquetas HTML , guardar titulos , numero de enlaces.

import requests

# Se install de la siguiete manera:
# python -m pip install beatifulsoup4

# Esta es la forma en que se importa
from bs4 import BeautifulSoup 



# Lo que busco es el USER_TOKEN
# Creo una funcion y le paso el SOurce
# Ya se que se trata de una sopa de beatifulsoup
def get_token(source):
    # Le indico a la libreria de Beatifulsoup el contenido y el parser que deeseamos utilizar. Esa es la sopa
    # Esta libreria depende de un parser, el mas utilizado es LXML porque soporta varios formatos
    # Podemos probar html.parser
    soup = BeautifulSoup(source, "html.parser") 
    # Para el token estoy buscando un input de tipo hidden y quiero sacar el valor.
    return soup.find('input',{'type':'hidden'})['value']


# NEcesito hacer un apeticion a la URL
# DOnde esta -----> Es el aplicativo web que intalamos en docker.
url = 'http://localhost:8083/login.php' 


#-------- REQUEST object
# Creo un objeto que sea un a session
# Esto lo hago para evitar que cada ve z que envie un reuqest me cambie el toke ID
# Me crea un objeto de session que utilizo para conctarme
# Se llamara S
with requests.Session() as s:
    # SImplemente saco la respuesta y de esa respuesta hago un print
    src  = s.get(url).text

    # Va mos a ver todo el codigo HTML con la inforamcion del usuario y las cookies de session
    # Lo mismo que hemos visto desde WIreshark
    #print(source)

    # Va mos a ver todo el codigo HTML con la inforamcion del usuario y las cookies de session
    # Lo mismo que hemos visto desde WIreshark
    #print(source)
    token = get_token(src)

    # Cada vez que hago una peticion cambia el token
    print(token)

    # -------- USER -PSW ---------------
    # Ahora envio un diccionario (clave,valor) con la information del formulario

    # Podemos regresar a mirar en wireshark donde tenemos los elementos fundamentales para realizar la peticion de tupo post.
    creds = {
        'username':'admin',
        'password':'password',
        'Login':'Login',
        # Como recojemos el token con nuestra funcion , le pasamos el source
        'user_token':token

    }

    # Ahora para realizar un apeticion post utilizamos la session a la URL con los datos que se le ingresan a continuacion.

    response = s.post(url,data = creds)

    print(response.text)