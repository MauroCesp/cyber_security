# PARAMIKO tienen su propia pagina con documentacion muy sencilla
# Es documentacion escrita para humanos
# PRimero tenemos que installarlo con pip install paramiko
import paramiko
from paramiko import SSHClient
import getpass


# Vamos a crear un cliente ssh que nos ejecute ordenes.
paramiko.util.log_to_file('paramiko.log') 
host = input("Introduce el host: ")
user = input("Introduce el usuario: ")
passwd = getpass.getpass("Introduce la contraseña: ")




# utilizo la clase SSHClient para crear un cliente
# Recordar que cuando se hace una connecion con SSH la primera vez nos pide el finger print
# Si no puedo validar el certificado que me estan dando 
# CUnado aceptamos el finger print se installa
client = SSHClient()

# La host key es el certificado que nos da el servidor
# Entonces utilizo una politica para validarlo
# RejectPolicy ------ Si no puedo validarlo no entro
#AutoAddPolicy ------ Automaticamente añade el certificado. Nuestro objeto le sale el mensaje y dice :" Si, si. Confio en el certificado"
# SI no cambio la politica queda por defecto RejectPolicy
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 

# Ahora nos conectamos 
client.connect(host,username=user,password=passwd)


# UNa vez conectados ejecutamos un comando
# En la documentacion encontramos todos los parametro que acepta la funcion
# EL metodo nos devuelve tres elementos
#
stdin, stdout, stderr = client.exec_command('ls -a')

# Aqui leo la informacion del STDOUT
for line in stdout.readlines():
	print(line)
 

# Cierro el cliente
client.close()
