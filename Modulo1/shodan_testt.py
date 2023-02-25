# pip install pyshodan
import shodan

# Utilizo esto para que no se muestre en pantalla el valor del key
import getpass


#----------- 1 --------------------
# Enviamos la informacion de la cuenta
# EL shodan Api es un objeto que cojemos de la cuenta de Shodan y lo metemos como parametro
def keyInformation(shodanApi):
    try:
        # Utilizo el metodo info para verificar si me connecto bien a mi Api key
        info = shodanApi.info()

        # Por cada elemento que encontremos en el array de informacion...
        for inf in info:
            print('%s: %s' %(inf,info[inf]))
    except Exception as e:
        print('Error: %s' % e)

#/----------- 2 --------------------
def shodanTest():
    try:
        
        shodanKeyString = getpass.getpass('Introduce tu api key:  ')

        #Aqui le tenemos que pasar el shodanAPI
        # Va a ser un objeto de la clase shodan donde le pasamos nuestra Apikey
        shodanApi = shodan.Shodan(shodanKeyString)
        print('Info del API')

        #Aqui llamo a la otra funcion
        keyInformation(shodanApi)

        # Ahora vamos a hacer lo mismo que se hace en la pagina de manera grafica
        # Le pasamos una query al buscador dependiendo de los filtros que queramos
        # La query si la metemos por un input
        query = input('Introduce el criterio de busqueda: ')

        # Llamo al objeto search y le paso la query
        results = shodanApi.search(query)

        print('---------------------------')
        print('Numero de resultados encontrados: {}'.format(results['total']))

        # Limitar el numero de resultados
        # results /// puede contener algo o no
        # Cuando contienen algo tiene un diccionario con una KEY que se llama MATCHES
        # Esto es lo que concide con la query
        # Lo pasamos a un alista y pillamos de la posicion 1 al que queramos mostrar

        # Creo lista para guardar los valores que le pasamos Nmap
        ip_list = []


            
        print('valores de las lista: ')
        for i in ip_list:
            print(i)
    except Exception as e:
        print('Error: %s' % e)

if __name__ == '__main__':
    shodanTest()

# AL final se puede buscar lo que se quiera.

#/----------- DBs expuestas sin ningun tipo de autehnticacion

## MongoDb -authentication

# Si conocemos lo que esconden las cabeceras de las distintas tecnologias que se utilizamos
# Se pueden plnatear busquedas mas avanzadas para llegar al resultados que buscamos

# ftp unp apache 

# podemos encontrar directamente tecnologias vulnerables

#--------------- Vulnerabilidades
# SI ya sabemos que hay una vulnerabilidad
# apache tienen una vulnerabilidad en su version 2.4 ///
    # apache 2.4.49
    