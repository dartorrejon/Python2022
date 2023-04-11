from os import strerror

try:
	file = open("C:/Users/darto/OneDrive/Documentos/Python2022/Ejercicios Python/POO-Ejercicios/Final_Python/cuentas.txt", "wt")
	for i in range(10):
		s = "linea #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("Se produjo un error de E/S:", strerror(e.errno))

#"C:/Users/darto/OneDrive/Documentos/Python2022/Ejercicios Python/POO-Ejercicios/Final_Python/cuentas.txt"

try:
    stream = open("C:/Users/darto/OneDrive/Documentos/Python2022/Ejercicios Python/POO-Ejercicios/Final_Python/cuentas.txt","rt")
    
    print(stream.read())
    
    stream.close()
except FileNotFoundError:
    print("No se encontro el archivo")



 #C:\Users\darto\OneDrive\Documentos\Python2022\Ejercicios Python\cuentas.txt
 


