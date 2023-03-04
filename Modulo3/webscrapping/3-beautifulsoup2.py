

from bs4 import BeautifulSoup, SoupStrainer
import requests


# Generamos una request
response = requests.get("http://thehackerway.com") 

# Se queire eviar los errores de cliente y de servidor
# Si no esta en esos reangos le pasamos el conternido y el parser 
if response.status_code not in range(400, 503):
    
    # De esta forma accedemos al contenido 
	soup = BeautifulSoup(response.content, "lxml")
	
 	# La funcion FINDALL nos recoge todos los elementos del tipo que queramos y le indiquemos
 	# miramos todas las URLS de etiqueta A que hay en toda la pagina.
  	# Tambien le indico que coja todos los que tengas un HREF para asegurarmnos que sean links
	for link in soup.find_all('a', href=True):
		# Regresamos el atributo que nos interesa
  
  		# De esta forma recojemos todos los enlaces que tienen un a pagina web.
		print(link['href'])
