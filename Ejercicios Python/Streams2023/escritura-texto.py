from os import strerror

# #Creamos una archivo nuevo
# try:
#     file = open("k:/python/archivo-stream/nuevo_texto.txt","w")
#     for i in range(10):
#         s = "numero "+str(i+1)+"\n"
#         for char in s:
#             file.write(char)
#             print(char,end='')
#     file.close()
#     print("\n\nArchivo creado con exito!")
# except IOError as e:
#     print(strerror(e.errno))


# #Mandar directamente un string en la funcion write tambien es posible
# try:
#     file = open('k:/python/archivo-stream/newtext.txt', 'wt')
#     for i in range(10):
#         file.write("línea #" + str(i+1) + "\n")
#     file.close()
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))



