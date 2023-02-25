import dns
import dns.resolver

# Es necesario installar la siguiente libreria sino no funciona
    # pip install dnspython


#/-------/ TIPO DE REGISTROS/-----------

#-----A
#Asocia un dominio con la maquina fisica donde se aloja ese dominio
# A este servidor DNS le estamos preguntando con que esta relacionado este dominio dentro de su base de datos 

assA = dns.resolver.resolve('ovid.com','A')
# Esto es solo para poner las lineas de division automaticas
print('.'*50)
print(assA.response.to_text())

#-----MX
# Mail Exchange---------- Dirige el correo que se envia al usuario que tiene registrado como servicio de correo para ese dominio

ansMX = dns.resolver.resolve('ovid.com','MX')
print('.'*50)
print(ansMX.response.to_text())

#-----NS
# Name server ---------- Determina los servidores que van a transmitir la informacion de un dominio

ansNS = dns.resolver.resolve('ovid.com','NS')
print('.'*50)
print(ansNS.response.to_text())


#-----AAAA
# Contienen la edicion IPV6 del A. Osea que son las IPV6 a las que esta relacionado el domino 

ansAAAA = dns.resolver.resolve('ovid.com','AAAA')
print('.'*50)
print(ansAAAA.response.to_text())

#---- TXT
# 

ansTXT = dns.resolver.resolve('ovid.com','TXT')
print('.'*50)
print(ansTXT.response.to_text())