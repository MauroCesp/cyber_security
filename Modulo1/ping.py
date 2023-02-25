
# La libreria  de subprocess la voy a utilizar mucho par realizar tareas de automatizacion
from subprocess import Popen, PIPE
import os 

# Defino un commando que deseo correr
program = "/bin/ping"

# Necesitamos saber si estamos trabajando con un sistema windows o Linux
# La sintaxis cambia un poco m'as
if os.name == 'nt':
	program = "ping"
iprange = input("introduce el rango de direcciones: ")
for ip in range(1,254):
	ipAddress = iprange+str(ip)
	print("Scanning %s " %(ipAddress))
	subprocess = Popen([program, '-c 1 ', ipAddress], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	stdout, stderr= subprocess.communicate(input=None)
	if "bytes from " in stdout.decode():
		print("The Ip Address %s has responded with a ECHO_REPLY!" %(stdout.decode().split()[1]))
		with open("ips.txt", "a") as myfile:
			myfile.write(stdout.decode().split()[1]+'\n')