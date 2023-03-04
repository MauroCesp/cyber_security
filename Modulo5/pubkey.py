'''
public key authentication:
keys:
				ssh-keygen -t rsa
copiar claves al servidor:
				ssh-copy-id user@host
'''


import paramiko
from paramiko import SSHClient
from paramiko import RSAKey
import getpass

paramiko.util.log_to_file('paramiko.log') 
host = input("Introduce el host: ")
user = input("Introduce el usuario: ")
passwd = getpass.getpass("Introduce la contraseña de la clave privada: ")

paramiko.util.log_to_file('paramiko.log')



#Se debe cambiar esta línea e incluir la ruta donde se encuentra la clave id_rsa
# Esta es la clave privada que authentica con la publica
private_key = '/home/adastra/.ssh/id_rsa'

# Con la clave privada vamos a caargar el contenido y crear un objeto de ella
# 
rsa_key = RSAKey.from_private_key_file(private_key,password=passwd)


# utilizo la clase SSHClient para crear un cliente
# Recordar que cuando se hace una connecion con SSH la primera vez nos pide el finger print
# Si no puedo validar el certificado que me estan dando 
# CUnado aceptamos el finger print se installa
client = SSHClient()

#client.load_system_host_keys()
# La host key es el certificado que nos da el servidor
# Entonces utilizo una politica para validarlo
# RejectPolicy ------ Si no puedo validarlo no entro
#AutoAddPolicy ------ Automaticamente añade el certificado. Nuestro objeto le sale el mensaje y dice :" Si, si. Confio en el certificado"
# SI no cambio la politica queda por defecto RejectPolicy
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 


client.connect(host, username=user, pkey=rsa_key,password=passwd)

# UNa vez conectados ejecutamos un comando
# En la documentacion encontramos todos los parametro que acepta la funcion
# EL metodo nos devuelve tres elementos
stdin, stdout, stderr = client.exec_command('ls -a')

# Aqui leo la informacion del STDOUT
for line in stdout.readlines():
	print(line)
