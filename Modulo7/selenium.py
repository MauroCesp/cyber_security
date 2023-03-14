# geckodriver hay que installarlo
# Esto es para FIREFOX
# installar selenium


from selenium import webdriver

# Esto es para utilizar las teclas
from selenium.webdriver.common.keys import Keys

# Esto es para utilizar el modulo de proxies
from selenium.webdriver.common.proxy import Proxy, ProxyType


# Esta funcion nos crea y nos devuelve el driver.
# Los parametros son personalizables
def getDriver(proxyserver=None, proxyport=None, proxyType="SSL"):
    
    # Lo pasamos en lower para controlar la entrada
	proxyType = proxyType.lower()
 
    # Cojemos el perfil de FIrefox
	fp = webdriver.FirefoxProfile()
 
 
 # Le decimo que si el proxy type es FTP , comenzamos a a justar las configuraciones
	if proxyType == "http":
        
		fp.set_preference("network.proxy.type", 1)
		fp.set_preference("network.proxy.http", proxyserver)
		fp.set_preference("network.proxy.http_port", int(proxyport))

		fp.set_preference("network.proxy.type", 1)
		fp.set_preference("network.proxy.ssl", proxyserver)
		fp.set_preference("network.proxy.ssl_port", int(proxyport))

    # SIla entrada no es FP, digamos que es SOCKS
	elif proxyType == "socks":
     # LE tenemos que indicar la version de sock que estamos utilizando
     # Igual que conTOR le indicamos el sock5
		fp.set_preference("network.proxy.socks_version", 5)
  
  # Con todo actualiza las configuraciones
	fp.update_preferences()
 
 # Qui ya tenemos el objeto y le pasamos las configuracion que acabamos de ingresar..
	return webdriver.Firefox(firefox_profile=fp)




# ya que tenemos configurado nuestro cliente de firefox podemo ejecutar alguna cosa en internet.
def check_exists_by_xpath(webDriver, xpath):
    try:
        webDriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True



# Aqui creamos nuestro objeto
webDriver = getDriver()

# Le paso un video y ya puedo hacer lo que quiera en el navegador.
# Tenemos que ver la pagina para entender lo que necesitamos ejecutar
# COn el inspector vemos el codigo HTML
webDriver.get("https://www.youtube.com/watch?v=tVjcotgB-uQ")

# Esto va a esperar por si tarda en contestar el servidor

#Es neesario revisar la documentacion para entender como las funcones llaman al codigo HTTP y lo ejecuta
webDriver.implicitly_wait(5)

genericAccept = check_exists_by_xpath(webDriver, '//*[@id="button"]')

if genericAccept:
	webDriver.implicitly_wait(15)
	webDriver.find_element_by_xpath('//*[@id="button"]').click()
webDriver.find_element_by_id("player-container").click()
print(webDriver.get_cookies())