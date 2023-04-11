from os import strerror

# #Creamos el archivo binario
# data = bytearray(10)

# for i in range(len(data)):
#     data[i] = 10 + i

# try:
#     binary_file = open('k:/python/archivo-stream/file.bin', 'wb')
#     binary_file.write(data)
#     binary_file.close()
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

# data = bytearray(10)
# #Leemos el archivo binario creado
# try:
#     binary_file = open('k:/python/archivo-stream/file.bin', 'rb')
#     binary_file.readinto(data)
#     binary_file.close()

#     for b in data:
#         print(hex(b), end=' ')
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))



# #Lectura de un archivo binario con la funcion read()
# data = bytearray(10)

# for i in range(len(data)):
#     data[i] = 10 + i

# try:
#     binary_file = open('file.bin', 'wb')
#     binary_file.write(data)
#     binary_file.close()
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

# try:
#     binary_file = open('file.bin', 'rb')
#     data = bytearray(binary_file.read())
#     binary_file.close()

#     for b in data:
#         print(hex(b), end=' ')

# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))



#Lectura de un archivo binario con la funcion read() con parametros
#data = bytearray(10)

# #Creamos el archivo
# for i in range(len(data)):
#     data[i] = 10 + i

# try:
#     binary_file = open('file.bin', 'wb')
#     binary_file.write(data)
#     binary_file.close()
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

# #Leemos el archivo binario
# try:
#     binary_file = open('file.bin', 'rb')
#     data = bytearray(binary_file.read(5))
#     binary_file.close()

#     for b in data:
#         print(hex(b), end=' ')

# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))



#Ejemplo de un programa para copiar y guardar un archivo
source_file_name = input("Ingresa el nombre del archivo fuente: ") #Buscamos el archivo origen
#abrimos el archivo
try:
    source_file = open(source_file_name, 'rb')
except IOError as e:
    print("No se puede abrir archivo fuente: ", strerror(e.errno))
    exit(e.errno)	

destination_file_name = input("Ingresa el nombre del archivo destino: ")#ingresamoe el nombre del archivo destino
#Tratamos de crear el archivo destino
try:
    destination_file = open(destination_file_name, 'wb')
except Exception as e:
    print("No se puede crear el archivo de destino:", strerror(e.errno))
    source_file.close()
    exit(e.errno)	

buffer = bytearray(65536) #Cargamos el buffer con 64 Bytes
total  = 0
#Tratamos de copiar el contenido del archivo origen al archivo destino.
try:
    readin = source_file.readinto(buffer)
    while readin > 0:
        written = destination_file.write(buffer[:readin])
        total += written
        readin = source_file.readinto(buffer)
except IOError as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) escritos con éxito')
source_file.close()
destination_file.close() #Cerramos todo
