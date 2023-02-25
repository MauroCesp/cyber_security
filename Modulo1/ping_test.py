
i


from subprocess import Popen, PIPE
import os 

program = "/bin/ping"
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