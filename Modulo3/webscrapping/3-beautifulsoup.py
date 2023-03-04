
# Beatiful soup lo que hace es ayudar a buscar informacion de una manera mas limpia
# Lo que hacemos es eliminar todo el HTML y guardar el contenido.
# Se pueden alterar el texto de las etiquetas HTML , guardar titulos , numero de enlaces.

# Se install de la siguiete manera:
# python -m pip install beatifulsoup4

# Esta es la forma en que se importa
from bs4 import BeautifulSoup 

# Los modulos que necesitamos para hacer nuestras peticiones: url, parser, http
import urllib.request, urllib.parse, urllib.error 
import urllib.request, urllib.error, urllib.parse 

# Inicializo una request y le paso el objetivo
url = urllib.request.urlopen("http://thehackerway.com") 

# De esta URl se coje el contenido
contents = url.read() 

# Le indico a la libreria de Beatifulsoup el contenido y el parser que deeseamos utilizar. Esa es la sopa
# Esta libreria depende de un parser, el mas utilizado es LXML porque soporta varios formatos
soup = BeautifulSoup(contents, "lxml") 

# Se extraen varias cosas por ejemplo
print(soup.title) 
# Cabeceras
print(soup.head) 

print(soup.body) 

# HTML body
print(soup.title .text)
