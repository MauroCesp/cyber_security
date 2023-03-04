# A veces cuando intentamos ir de un punto A a un punto B 

# A -   PIVOTE        B
# A -------------x ---B
# A ---------PIVOTE --B

# Si la paso por la maquina PIVOTE el trafico si que llega en ambos sentidos.
# Esto es lo que se llmaa port forwarding
# El pivote se pega al puerto que queremos y le creamos una regla de forwarding
#  Se hace indicandole al PVIOTE que todo el trafico que llegue en el puerto 9000 se reenvi a la maquina B al puerto que queramos.
# PIVOTE tienen 2 tuplas (IP_PIVOTE, 9000)   (IP_B, 3389)



import os
import socket

import threading

# Crea run server socket

                # A ----> PIVOTE
sserver = socket.soclet(socket.AF_INET, socket.SOCK_STREAM)
sserver.bind("0.0.0.0", 9000)

# Ahora le ponemos que podamos se guir aceptando peticiones
sserver.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR,1)

# S e queda a la escucha

sserver.listen(10)

sserver.settimeout(1)


                # B (PIVOTE----> B)
# Ahora vamos a crear una serie de hilos para saber quien envia que
# Camino de ida y vuelta en ambos sentidos.

while True:
    sclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Esperamos a la connecion de A al PIVOTE
        # Auqi lo que recibimos es un soclet y la IP de la coneccion
        # Aqui ya tenenmos un socket abierto
        socketA, addressA = sserver.accept()
        
        
        socketB = sclient
        
        # OCnneccion de PIVOTE con B
        socketB.connect(("172.23.153.99",3389))
     
        # Lo creamos asi para que lo que me llegue por socket A lo pueda enviar por socket B    
        t1 = threading.Thread(target = traffic, args(socketA, socketB))
        t1.start()
        
        t2 = threading.Thread(target = traffic, args(socketB, socketA))
        t2.start()
        
    except:
        pass
    
    
    
    
    def traffic(a,b):
        
        # Aqui recibo los dos soclets que cree m{as arriba}
        # Pillo el trafico en ambos sentidos
        src = a.getsockname()[0]
        dst = b.getsockname()[0]
        
        
        while True:
            
            try:
                # Leo del socket A y cunado reciba datos del socket A los envia a traves del socket B
                # Y de igual manera cunado el trafico va del lado contraripo
                # Por eso necesito dos hilos que los cree mas arriba
                buff = a.recv(2048)
                if len(buff) != 0:
                    b.send(buff)
                    
            except socket.error:
                print("Soket error!")