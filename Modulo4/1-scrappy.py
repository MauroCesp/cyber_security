# Vamos a hacer un syn scann que es un tipo de escane oq ue se utiliza para saber
# SI una maquina tinen un puerto abierto o no.

# Si el puerto esta cerrado  RST + ACK


from scapy.all import *
# para ver todos los campos que tiene  el modulo
        #ls(TCP)
        
# Construimos un paquete
dport = 80

# -------- CAPA DE TRANSPORTE -------------------
# ENvio una peticion para saber si el puerto 80 esta abierto
# sprt - es el puerto de origen si no lo indico le pone un o por default
# Queremos habilitar varias flags.
# Esto lo que hace es crear la capa TCP y guardarla en la variabel
tcp = TCP(dport= dport, sport=3000,flags='S')

# -------- CAPA IP
# TTL --------- Time TO Leave
# Esto es para que un paquete no se qude dando vueltas eternametne entre routers.
# EL router por donde pase detecta este field y cuando llegue a 0 el router lo desecha
ip = IP(dst="172.23.151.23", ttl = 60)

# IP es el protocolo general que contienen todo el paquete
# TCP va dentro del campo de IP
packet = ip/tcp

respuesta = sr(packet,timeout=1)

# la respusta sera una tupla con la inforamcion enviada y recibida
# Tenemos que sleccionar que parte de la respuesta queremos
# Si tenemos respuesta nos quedamos con el primer packete 001 HAS LAYER
# FIltramos si tienen capa TCP o no
# Si teine capa TCP siginifica que me estan respondinedo mi peticion
if respuesta[0][0][1].haslayer(TCP):
    
    # SYN -S
    # ACK - A
    # RST - R 
    # FIN - F
    # Asi es como construyo la respuesta que me envianS y veo lo que me envian
    if respuesta[0][0][1]['TCP'].flags== 'SA':
        print('puerto abierto')
    else:
        print('puerto cerrado')
        
        # Print los flags para saber la respuesta que se ecibio y porque esta el puerto cerrado.
        print(respuesta[0][0][1]['TCP'].flags)



 
 