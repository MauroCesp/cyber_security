#!/usr/bin/python 
 
import hashlib

# En esta funcion 
def hashMD5(plainText):
    result = hashlib.md5(plainText)

     # En lugar de devolver el texto plano lo puedo presentar de varias maneras
    # Hexadecimal
    resultHex = str(result.hexdigest())

    print(plainText.decode(encoding='UTF-8'))

    # BYTES
    # Hacemos un digest normal y nos regresa los bytes 
    print(str(result.digest()))
    return resultHex


if __name__ == "__main__":

    # Aqui buscamos que el string sea binario
    # Para eso se le pone una B adelante del string
    # Asi la funciona de hash funciona, sin eso no
    plainText = b'Hola'
    
    print(hashMD5(plainText))


 

