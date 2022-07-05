numeros = []
suma=0
entrada = int(input("Ingrese un numero entero para sumar[FIN = 0]: "))


while entrada != 0:
    numeros.append(entrada)
    entrada = int(input("Ingrese otro numero para sumar[FIN = 0]: "))



if len(numeros)!=0:
    for i in range(len(numeros)):
        suma += numeros[i]
        
    prom = suma/len(numeros)
    print("El promedio de los numeros ingresados es: ",prom)
else:
    print("No ingreso ningun numero!")

print("Fin del programa!! =)")