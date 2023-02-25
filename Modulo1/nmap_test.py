import nmap
# python -m pip install python-nmap

# pip install pyshodan
import shodan

# Utilizo esto para que no se muestre en pantalla el valor del key
import getpass


# Aqui guardo toda la informamcion del host.
class NmapHost:
    def __init__(self):
        self.host = None
        self.state = None
        # La razon del porque un servicio esta activo
        self.reason = None

        # Estos son arrays de puertos que los trabajamos en otra clase.
        self.openPorts = [] 
        self.closedFilteredPorts = [] 


# Aqui gusrdo los traitbutos de los puertos que recibo por NMAP
# Inicializo todo con NONE porque puede que no recibas la informacion completa
class NmapPort:
    def __init__(self):
        self.id = None
        self.state = None

        #  La razon del porque el puerto esta abierto o cerrado.
        self.reason = None
        self.port = None
        self.name = None
        self.version = None
        self.scriptOutput = None


# Aqui recibo un escaneo que voy a parsear
# Esto es para tener una vista mas detallada y bonita en Python
def parseNmapScan(scan):

    # Inicicalizo una variable conlos hosts que haya podido escanear NMAP
    # Y recorrermos cada host
    nmapHosts = []

    # La funcion ALL)HOST me regrsa todas llos host
    #A
    for host in scan.all_hosts():

        # AHora creo un objeto nmap para guardar la info
        nmapHost = NmapHost()

        # Ahora asigno el HOST
        # EL host sera el host aque estamos recorriendo

        nmapHost.host = host


        # SI existe un STATUS en el escaneo...
        if 'status' in scan[host]:

            # Recojemos los atributos del host actual  dentro del state actual
            # -------------------Guardo la siguiente info:

            # name
            # product
            # version
            # extrainfo

            nmapHost.state = scan[host]['status']['state']
            nmapHost.reason = scan[host]['status']['reason']

            # ----------- RECORRER PROTOCOLO  -----------------
            # Dentro del objeto que recorremos encontramos varios protocolos 
            #  UDP , ICMP, TCP
            # Por cada un od eellos vamos a ver si el host tienen al guno de ellos
            for protocol in ["tcp", "udp", "icmp"]:
                
                # Si encuentro uno de estos protocolos en cada vuelta:
                if protocol in scan[host]:

                    # Extraigo los puertos que se encuentren en esos protocolos
                    # La lista va a tener las claves
                    ports = list(scan[host][protocol].keys())

                    # Por cada puerto que encuentre defino una variable de tipo NMAP PORT ppara almacenar informaion en ella.
                    for port in ports:
                        nmapPort = NmapPort()

                        # Y le asigno el puerto que estoy recorriendo
                        nmapPort.port = port

                        # Ahora el State 
                        nmapPort.state = scan[host][protocol][port]['state']


                        #--------SCRIPT-----------------
                        if 'script' in scan[host][protocol][port]:
                            nmapPort.scriptOutput = scan[host][protocol][port]['script']

                        #--------REASON-----------------
                        # Si existe una razon para este puerto
                        if 'reason' in scan[host][protocol][port]:
                            nmapPort.reason = scan[host][protocol][port]['reason']
                        #--------NAME-----------------
                        if 'name' in scan[host][protocol][port]:
                            nmapPort.name = scan[host][protocol][port]['name']
                        
                        #--------VERSION-----------------
                        if 'version' in scan[host][protocol][port]:
                            nmapPort.version = scan[host][protocol][port]['version']

                        #--------OPEN-----------------
                        if 'open' in (scan[host][protocol][port]['state']):

                            # Si el puerto esta abierto lo meto en mi lista de puerto abierto que defini al principio
                            nmapHost.openPorts.append(nmapPort)
                        else:
                            # Si el puerto no esta abierto lo metemos en el la lista de lo spuertos cerrados.
                            nmapHost.closedFilteredPorts.append(nmapPort)


                    #--------LISTA HOST
                    # Cuando ya hemos terminado con el escaneo lo meto denrto del objeto que cree.    
                    nmapHosts.append(nmapHost)
        else:
            print(("[-] There's no match in the Nmap scan with the specified protocol %s" %(protocol)))

        # Ahora cojo el objeto NMAP host y lo envio
        return nmapHosts

def run_nmap_scan(ip_list):

    nm = nmap.PortScanner()

    # Recorremos la lista de ip que recibimos por parametro
    for i in ip_list:
        nm.scan(i, '22')

        # Vamos a parserar el objeto NMAP para que tenga mejor formato
        # 
        structureNmap = parseNmapScan(nm)


        for host in structureNmap:
            try:
                print("Host %s " %(host.host))
                print("State %s " %(host.state))
                print("Reason %s " %(host.reason))
                print("Ports: ")
            except:
                pass

            # Ahora imrpimo la informacion de cada puerto abierto que encontremos.
            for port in host.openPorts:
                try:
                    print('Puertos abiertos econtrados: ')
                    print('--------------------------')
                    print("     Number: %s " %(port.port))
                    print("     Name: %s " %(port.name))
                    #print("     Version: %s " %(port.version))
                except:
                    pass
            print('--------------------------')
            print(' ')

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

        # LE solicicto al usuario una API key por pantalla
        shodanKeyString = getpass.getpass('Introduce tu api key:  ')
        # Aqui le tenemos que pasar el shodanAPI
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

        # Obtengo cinco valores y los agrego a la lista
        for result in list(results['matches'])[1:6]:

            if ':' in result:
                pass
            else:
                ip_list.append(result['ip_str'])

            #print('---')
            #print('IP: %s' % result['ip_str'])
            #print(result)
        # Llamo a la funcion para tomar la informacion de la lista in realizar el nmap con las ips
        run_nmap_scan(ip_list)

    except Exception as e:
        print('Error: %s' % e)


# Creo la funcion principal.
if __name__ == '__main__':
    shodanTest()