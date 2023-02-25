# SUBPROCESS es una libreria que nos permite llamar linea de codigo en terminal y obetenr respuesta a traves de STDOUT
# Si estamos escaneando una red completa no podemosir ip por ip llamandolas una a una
# Atraves del metodo CALL vamos a trabajar

# Voy a llamar un comando desde terminal ---- el comando se instancia como array

# command = ['cat ','/etc/shadow']
# EN shadow se alojan las contrase;as y los hashes de los usuarios de Linux---- Pide sudo

import subprocess

param = '-listar'
filepath = '/etc/'

# Ahora defino el comando que quiero llamar de la terminal

# LE decimos que queremosque muestre la lista de usuarios y sus hashes
command = ['ls',param, filepath]

# Ahora utilizamos subprocess para ejecutar el comando.
# SI lo ejecuto asi me va a pedir SUDO
# ENtonces para probarlo los intentamos con un SUDO SU
subprocess.call(command)