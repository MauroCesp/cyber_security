import scanless
import json


# Esta herramient utiliza scanners que estan disponibles ONLINE
# Tenemos que definir el tipo de scanner que queremos utilizar.
# De esta maner lo hacemos de alguna manera ANONIMAMENTE
# Inicializo una variable scanless
sl = scanless.Scanless()


# Me va a dar una enumeracion de puertos que stan abiertos , es decir el finger print
output = sl.scan('scanme.nmap.org', scanner = 'ipfingerprints')

results = json.dumps(output['parsed'], indent=2)

print(results)