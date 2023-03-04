from scapy.all import *

# Esto entra en la parte de descubrimiento de MAQUINAS EN UNA RED
# Es una alternativa a PING y CNPpara obtener la direccion fisica MAC de mi maquina y la IP
# Utilizo las funciones GET_IF 

# Se envia un ARP request
# Se envia un BROADCAST lo que significa que todas las maquinas la vana a escuchar
# PEro solamente reposnde la que tenga la MAC y la IP
# ENtrega la direccion fisica
# Asi se puede conseguir las direcciones fisicas que tienen las direcciones IP que se consigan.

# Toda la info que usamos aqui es la que sale con IPCONFIG
mymac = get_if_hwaddr("eth1")
myip = get_if_addr("eth1")


# PEro realmente lo que buscamos no es la direccion fisica sino si estas DESPIERTAS
# # Construyo un paquete ARP request (ETHER) porque trabajamos con la capa de enlace
# DST --- Destino, Pone la direccion fisica
# ARP ---- hwsrc (hardware source--direccion donde viene ORIGEN) --- hwdst(hardware destiny -- direccion don de tienen que llegar la respuesta)
#
arp_request= Ether(dst=ETHER_BROADCAST)/ARP(hwsrc=mymac, hwdst= ETHER_BROADCAST, pdst="172.23.151.23")

arp_reply = srp(arp_request, timeout=1)
# Ahora lo intento indexar# SI la tupla existe y tiene el campo 0 la maquina esta viva
if arp_reply and arp_reply[0]:
    print("maquina viva")
else:
    print("N MAC found")

