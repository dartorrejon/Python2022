# from operator import invert


# nombres = []
# apellidos = []
# dato = ""
# fin = False

# while not fin:
#     dato = input("Ingrese su nombre: ")
#     if dato != "1":
#         nombres.append(dato)
#         dato = input("Ingrese su apellido: ")
#         apellidos.append(dato)
#     else:
#         fin = True

# if len(nombres) != 0:
#     for i in range(0,len(nombres)):
#         print("Hola "+nombres[i]+" "+apellidos[i])
# invertido = nombres.reverse()
# ordenado = apellidos.sort()
nombres = ["maria","pablo","dario","Kevin","Alberto","cristina"]
apellidos = ["Torrejon","Perea","Martinez","Kirchner","Alonso","Zamboni","Caceres"]
nom_rev = nombres[:]
nom_rev2 = nombres[::-1]
nom_rev.reverse()
print(nombres)
print(nom_rev2)
print(nom_rev)
print(apellidos)
apellidos.sort()
print(apellidos)
apellidos.remove("Perea")
print(apellidos)
for i in nom_rev2:
    print(i)

ape_st = str(apellidos)
print(type(ape_st))
print(ape_st)

print("\n"*50)
print("Mostramos la salida de la funcion creada:")
def mostrarNomyApe(ap, nom):
    for i in ap:
        print(i)
    for j in nom:
        print(j)

mostrarNomyApe(nombres,apellidos)
eliminado = apellidos[3]
print("Apellido eliminado de la lista: "+eliminado)
print(len(nombres))
print(len(apellidos))
apellidos.insert(0,1)
print(apellidos)
nombres.insert(0,"Carloncho")
print(nombres)
nombres.insert(-1,"teresita") #Insrta un valor moviendo el valor de esa posicion a la derecha
print(nombres)
nombres.append("Fererico") #Agrega un elemento al final de la lista
print(nombres)

print("Bueno por fin terminamos el ejerccio carpincho....=)")