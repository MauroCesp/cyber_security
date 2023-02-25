# SUBPROCESS es una libreria que nos permite llamar linea de codigo en terminal y obetenr respuesta a traves de STDOUT
# Si estamos escaneando una red completa no podemosir ip por ip llamandolas una a una
# Atraves del metodo CALL vamos a trabajar

# Voy a llamar un comando desde terminal ---- el comando se instancia como array

import subprocess


# El los sistema windows los comnados son diferentes
# NEcesitamos un script que fucione para los dos y nos diga en que sistema estamos.
# Para ello vamos a utilizar PLATFORM
# TIenen una funcion que se llma SYSTEM nos dice en que sistem operativo estamos trabajando.
import platform


def ping(host, n_packs):
    # Creo una funcion que reciba por parametro una IP
    # Defino los comandos que le paso al ping
    #host = '192.168.1.1'

    # ----LINUX va a ser por defecto
    param = '-c'

    # Pero ahora averiguo la paltaforma con el modulo de platform
    # Lo pasamos todo a minuscula por si hay algun cambio entre sistemas
    plat = platform.system().lower()

    if (plat == 'windows'):
        #---- WINDOWS
        param = '-n'
    

    # Ahora defino el comando que quiero llamar de la terminal

    # LE decimos que queremosque muestre la lista de usuarios y sus hashes
    command = ['ping',param, n_packs, host]

    # Ahora utilizamos subprocess para ejecutar el comando.
    # SI lo ejecuto asi me va a pedir SUDO
    # ENtonces para probarlo los intentamos con un SUDO SU
    subprocess.call(command)

if __name__ == '__main__':

    host = input('Introduce base IP: ')
    n_packs = input('Intrudce cuantos paquetes a enviar: ')

    rango = int(input('Rango de IPS: ej 254 '))

    # Como oq eu quiero es recorrer un rango de IP hago un FOR para recorrer el rango que ingresa el ususario
    for i in range(rango):
        # Convierto la host con cada uno de los numero del rango
        target = host+str(i)

        # Repito lo mismo 
        if(i>0 and i<255):
            ping(target, n_packs)




