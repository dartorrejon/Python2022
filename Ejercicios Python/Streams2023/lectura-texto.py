from os import strerror

# #Cargar el archivo a 1 caracter a la vez y luego recorrerlo con un while
# try:
#     contenido = open("k:/Python/Archivo-Stream/texto.txt","rt")
#     char = contenido.read(1)
#     cont=0
#     while char != '':
#         print(char,end='')
#         cont +=1
#         char=contenido.read(1)
    
#     contenido.close()
#     print("\n\nLa cantidad de letras que caracteres que contiene el texto es:",cont)
# except IOError as exc:
#     print(strerror(exc.errno))


# #Cargar todo el archivo a la vez y luego recorrerlo con un for
# try:
#     texto = open("k:/Python/archivo-stream/texto.txt","rt")
#     contenido = texto.read()
#     counter = 0
#     for char in contenido:
#         print(char,end="")
#         counter+=1
#     texto.close()
#     print("\n\nLa cantidad de caracteres del texto es:",counter)
# except IOError as exc:
#     print(strerror(exc.errno))


# #Cargar archivo linea por linea y luego recorrerlo con wile y for
# try:
#     counter=0
#     lcounter=0
#     stream = open("k:/python/archivo-stream/texto.txt","rt")
#     texto = stream.readline()
#     while texto!='':
#         for char in texto:
#             print(char,end='')
#             counter +=1
#         lcounter+=1
#         texto= stream.readline()
#     stream.close()
#     print("\n\nLa cantidad de lineas en el texto es de:",lcounter)
#     print("La cantidad de caracteres del texto es:",counter)

# except IOError as exc:
#     print(strerror(exc.errno))


# #Cargar el archivo de a varias lineas a la vez y luego recorrerlo con 
# try:
#     stream = open("k:/python/archivo-stream/texto.txt")
#     contenido = stream.readlines(20)
#     lcounter=0
#     counter=0
#     print(type(contenido))
#     while contenido != []:
#         for line in contenido:
#             lcounter +=1
#             for char in line:
#                 print(char,end='')
#                 counter +=1
#         contenido = stream.readlines(10)
#     stream.close()
#     print("\n\nLa cantidad de lineas del texto son:",lcounter)
#     print("La cantidad de caracteres del texto es:",counter)
# except IOError as e:
#     print(strerror(e.errno))


#Leyendo un archivo en MODO TEXTO a travez de la funcion open() ya que devuelve un objeto que es instancia de la clase iterable
try:
    counter = lcounter = 0
    for line in open("k:/python/archivo-stream/texto.txt","rt"): #leemos linea por linea
        lcounter +=1
        for char in line: #leemos caracter por caracter
            print(char,end='')
            counter +=1 #No hace falta cerrar el stream...lo hace automaticamente
    print("\n\nLa cantidad de lineas del texto es:",lcounter)
    print("La cantidad de caracteres que contiene el texto es:",counter)
except IOError as e:
    print(strerror(e.errno))