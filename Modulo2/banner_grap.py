import socket
import sys

# Vamos a establecer unavariable que contenga nuestro fichero de puertos
# Este es un archivo .txt en la misma ruta, de damos permisos de lectura
ports = open('./ports.txt', 'r')

# Ahora hago un array con los puertos vulnerables

vulnbanner =[]

# Por cada banner que aparezca lo almacenamos en el fichero.
with open('./vulnbanner.txt','r') as vulnbanner_txt:
    for line in vulnbanner_txt:
        vulnbanner.append(line)

# Ahora por cada puerto de nuestra lista lo recorremos 

for port in ports:
    #inicializamos un socket server
    # Utilizamos la clase socket pero tienen un constructor que tienen que inicializarse
    # Es necesario especificar la familia de direcciones y solo se puede utilizar esa familia
    # Despues le especificamos el SOCK stream, transmite los datos en orden de forma fiables
    # Se le conoce como un PIPE stream *( tuberia)
    print('Looking for port: '+ port)
    # AF_INET4 lo tenemos que especificar
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # PUeden pasar muchas cosas como que conecte o no, para eso utilizo try except
    try:
        print('Connecting to '+ str(sys.argv[1]) + ':'+ port)
        #Conecto mi socket
        # LE pasamos un a IP y un puerto dentro de un mismo objeto

        sock.connect((str(sys.argv[1]), int(port)))
        sock.settimeout(1)

        # Ahora lo que recibo son los datos de banner con receive
        banner = sock.recv(1024)

        # Ahora podemos sacar el nombre del banner
        # Como lo que recivimos esta codificados neecesitamos hacer un decode.
        # Tambien lo paso a string pra utilizalo en una comparasion mas adelante
        # COmparo estos datos de banner con los de la lista.
        bannerName = str(banner.decode().strip())

        # Ahora recorro la lista de banners
        for i in vulnbanner:
            print(' Is' + bannerName.lower().strip() + 'in' + i.lower().strip())
            # Le quitamos los espacios y lo pasamos a lower case lo que encontremos
            if i.lower().strip() in bannerName.lower().strip():

                print('Banner found: '+ bannerName)
                print('Host: '+ str(sys.argv[1]))
                print('Port: '+ str(port))


    except Exception as e:
        print('Error: '+str(e))
        # EN caso de que algun puerto no de problemas
        continue
        # Si salta una exception nuestro socket se cierra para que no quede pillado.
        sock.close()
    finally:
        # En caso de que ocurra algo inesperado cerramos nuestro socket asi tambien para asegurarnos
        if sock is not None:
            sock.close()