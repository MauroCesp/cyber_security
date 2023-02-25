class NmapHost:
    def __init__(self):
        self.host = None
        self.state = None
        self.reason = None
        self.openPorts = [] 
        self.closedFilteredPorts = [] 

class NmapPort:
    def __init__(self):
        self.id = None
        self.state = None
        self.reason = None
        self.port = None
        self.name = None
        self.version = None
        self.scriptOutput = None

def parseNmapScan(scan):
    nmapHosts = []
    for host in scan.all_hosts():
        nmapHost = NmapHost()
        nmapHost.host = host
        if 'status' in scan[host]:
            nmapHost.state = scan[host]['status']['state']
            nmapHost.reason = scan[host]['status']['reason']
            for protocol in ["tcp", "udp", "icmp"]:
                if protocol in scan[host]:
                    ports = list(scan[host][protocol].keys())
                    for port in ports:
                        nmapPort = NmapPort()
                        nmapPort.port = port
                        nmapPort.state = scan[host][protocol][port]['state']
                        if 'script' in scan[host][protocol][port]:
                            nmapPort.scriptOutput = scan[host][protocol][port]['script']
                        if 'reason' in scan[host][protocol][port]:
                            nmapPort.reason = scan[host][protocol][port]['reason']
                        if 'name' in scan[host][protocol][port]:
                            nmapPort.name = scan[host][protocol][port]['name']
                        if 'version' in scan[host][protocol][port]:
                            nmapPort.version = scan[host][protocol][port]['version']
                        if 'open' in (scan[host][protocol][port]['state']):
                            nmapHost.openPorts.append(nmapPort)
                        else:
                            nmapHost.closedFilteredPorts.append(nmapPort)
                    nmapHosts.append(nmapHost)
        else:
            print(("[-] There's no match in the Nmap scan with the specified protocol %s" %(protocol)))
        return nmapHosts

if __name__ == '__main__':
	nm = nmap.PortScanner()
	nm.scan('127.0.0.1', '22')
	structureNmap = parseNmapScan(nm)
	for host in structureNmap:
		print("Host %s " %(host.host))
		print("State %s " %(host.state))
		print("Ports: " )
		for port in host.openPorts:
			print("Number: %s " %(port.port))
			print("Name: %s " %(port.name))
