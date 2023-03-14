# La forma mas sencilla de efectiva de romper un hash es por FUERZA BRUTA
# TIramos contrase;as con un diccionario y cada una la hasheamos
# SI son iguales dimos con la contrase;a
# Para hacer esto se necesita saber el tipo de hash que se utiliza
# LO malo es que el proceso se lleva mucho tiempo

# TABLAS DE BUSQUEDA  son mas efecientes porque contiene una serie de cadenas de texto  ya hechas

# Para la practica accedemos a un servidor que tienen una tabla de has de un  numero de telefono
# Se hace un a taque por fuerza bruta de manera aleatorio a los hashes
#!/usr/bin/python 
 
import hashlib

import random


# Lo primero es realizar un hash


# En esta funcion crea un hash
def hashMD5(plainText):
    result = hashlib.md5(plainText)

     # En lugar de devolver el texto plano lo puedo presentar de varias maneras
    # Hexadecimal
    resultHex = str(result.hexdigest())
    return resultHex


# ENtonce para este ejercicio utilizamos una funcion que adivine el hash que conseguimos para sacarle el contenido.
# Se crea una funcion que se llama BRute  y recibe como parametro un determinado hash

def bruteForce(givenHash):
    # Se declara una lista de nuemros porque es un numero
    # Pero tambien podria ser letrs si es una contrase;a

    numbers = '1234567890'
    numbers_list = list(numbers)

    # La ejecucion se para cunado se encuentra el numero correcto

    while(True):

        # Se meten numeros de manera aleatoria de cuatro digitos(porque para el ejercicio es un PIN lo que se quiere averiguar)
        # Utilizamos la funcion cices y le pasamos la lista de nuemros . Se le dice que tome cuatro.
        toHash = random.choices(numbers_list, k =4)

        # Es necesario pasarlo a BINARY strig
        # Se toma la variable toHash y se a;ade un JOINT para como si fuera string
        # Ya convertido se le pasa a la funcion de hashear * hashMD5

        toHash = ''.join(toHash).encode()

        print(toHash.decode())

        # Ahora se hashea
        result = hashMD5(toHash)

        # Ahora si este hash conicide con el que se realiza aqui se ha encontrado la password.

        if(givenHash == result):
            print('Password is: ' + str(toHash.decode()))
            break


if __name__ == "__main__":
    
    print('-'*40)
    action = str('Indique que desea realizar:')
    print('-'*40)
    print('1- Crear HashMD5')
    print('2- Romper hashMD5')
    
    print('-'*40)

    # Aqui buscamos que el string sea binario
    # Para eso se le pone una B adelante del string
    # Asi la funciona de hash funciona, sin eso no
    givenHash = '01a0683665f38d8e5e567b3b15ca98bf'
    
    bruteForce(givenHash)
