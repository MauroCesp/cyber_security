
# Primero installa la libreria
    # sudo apt-get install tor
#· Se inicializa el servicio
    # sudo service tor start
# Se levanta un servicio en el puerto 9050
# Hay una pagina que se llama detector.tor que te dice si se esta utilizando TOR
import requests

# Recurso que nos identifica
url = "https://ident.me"

# Aqui aun no se interactua con TOR
response = requests.get(url).text
print(response)

# Esto es solo para asegurar que hay coneccion
# Ahora se realizan las peticiones atraves de los proxies
# Se deben de asignar los proxies
# Sock5 es el tipo de  que utliza TOR
proxies = {'http': 'socks5h://127.0.0.1:9050',
			'https':'socks5h://127.0.0.1:9050'}

# A la peticion le indica que los proxies que se van a utilizar son los que se acaban de definir 
#response1 = requests.get(url, proxies=proxies).text  

# Aqui es la IP una vez que  se interactua con TOR
#print(response1)      

# Para asegurarnos que la conexion sea completamente anonima installamos un fake user agent.
    #python -m pip install fake_useragent
# Importamos un user agent

from fake_useragent import UserAgent

# La info se pasa a traves de las cabeceras
# Se toma el user agent y se le pide un random
# Esto da distintos user agents(browsers de peticion diferentes), que se combina con TOR
# Esto es especialmente importante cuando se hace webscrapping y no se quiere que se vete la ip que se utiliza 
headers = {'User-Agent': UserAgent().random}
print(headers)
response1 = requests.get(url, proxies=proxies, headers=headers).text
print(response1)