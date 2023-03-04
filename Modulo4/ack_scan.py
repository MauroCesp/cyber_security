# Vamos a hacer un ACK scann que es un tipo de escane oq ue se utiliza para saber
# SI una maquina tinen un puerto FILTRADO
# Es decir si existe un firewall o no


from scapy.all import *
# para ver todos los campos que tiene  el modulo
        #ls(TCP)
        
# Vamos a enviar un paquete al puerto 81 porque siempre esta cerrado
# Vamos a esperar la respuesta
# RST ------ NO FILTRADO
# IMCP ------ Firewall
# Cualqueri otro mensaje de timeout es el firewall
dport = 81

# -------- CAPA DE TRANSPORTE -------------------
# ENvio una peticion para saber si el puerto 80 esta FILTRADO
# sprt - es el puerto de origen si no lo indico le pone un o por default
# Queremos habilitar vla flag de ACK
# Esto lo que hace es crear la capa TCP y guardarla en la variabel
tcp = TCP(dport= dport, sport=3000,flags='A')

# -------- CAPA IP
# TTL --------- Time TO Leave
# Esto es para que un paquete no se qude dando vueltas eternametne entre routers.
# EL router por donde pase detecta este field y cuando llegue a 0 el router lo desecha
ip = IP(dst="172.23.151.23")

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
    # SI me devuelvae R significa que NO hay firewall
    if respuesta[0][0][1]['TCP'].flags== 'R':
        print('puerto no filtrado')
else:
    print('puerto filtrado')
        
    # Print los flags para saber la respuesta que se ecibio y porque esta el puerto cerrado.
    print(respuesta[0][0][1]['TCP'].flags)



 
 