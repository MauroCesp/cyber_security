import subprocess
import platform

# Defino una funcion para determinar. si el sistema operativo es Linux o WIndows
# Para eso utilizamos param

def ping(host, n_packets):
    # C significa Linux y si no es entonces sera un windows
    # ALgunas vees vienen en mayuscula o minuscula entonces lo pasamos a minuscula
    plat = platform.system().lower()

    # Param es por defecto C
    param= '-c'

    # pero si recibo windows por parametro lo pongo como N
    if(plat == 'windows'):
        param= '-n'

    command = ['ping',param, n_packets,host]
    subprocess.call(command)

if __name__ == "__main__":

    # Dejamos la direccion asi para que el numero final sea el rango que introduce el usuario
    host = input('Introduce el host: 192.168.1.')
    n_packets = input('Introduce el numero de paquetes')

    # Esto lo hago para definir un rango que deseamos recorrer
    rango = int(input('Introduce el rango:e.x 254'))

    for i in range(rango):
        target= host+str(i)

        if(i>0 and i<255):
            ping(target, n_packets)