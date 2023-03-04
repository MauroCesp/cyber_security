import urllib.request

response ¿ urllib.request.urlopen("https://www.google.com")

print(response)

code = response.getcode()

url = response.geturl()

print("Code: "+str(url))

# Lo que hago aqui es recorrer los heder que regresa la cosulta
# COmo regresa un diccionario lo recorro asi
for header, value in list(response.headers.items()):
    print(header + ":"+value)