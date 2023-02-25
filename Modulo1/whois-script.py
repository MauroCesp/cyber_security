#IMporto la libreria
import whois

# Creo un objeto con el modulo WHO is 
who = whois.whois('ovid.com')
#----- TRUCO---------
# Cuando no se sabe cuales son las funcniones en una libreria que no conocemos 
# Utilizamos la funcion DIR y le pasamos el modulo como parametro
#--------print(dir(who))

# Ahora imprimimos el diccionario de valores que nos devuelve.
# Todo lo que existe sobre el dominio o el .com

#----------TODOS
print('values:'+str(who.values()))

#---------- Solo las llaves
#print('Keys'+str(who.keys()))

#---------- Solo un valor(key)
#print(str(who['registrar']))



#---------------------------------------------------------
#------- Datos importantes para descubrri vulnerabilidades
#---------------------------------------------------------

#---------- SOlo un valor(array)
#print(str(who['creation_date'][1]))
#print(str(who['expiration_date'][1]))

# Tambien el nombre de los servidores en un dato importante para ir agrandando el mapa de donde estan las vulnerabilidades.
# El estado del servidor tambine es importante.