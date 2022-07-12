'''Necesitamos un programa que permita sumar todos los números primos que existen hasta el número 1000. 
Luego presentar el resultado de esa suma en consola.

Sugerencia: Reutilizar el código realizado en clase para determinar si un número es primo como una
 función que es llamada desde el programa principal. Emplear un bucle for para realizar el proceso.'''
#Variables
sum=0

#Definimos la funcion para saber si un numero es primo o no
def es_primo(a):
    cont =1
    pri=0
    
    while(cont <= a and pri<=2):
        if(a%cont==0):
            pri+=1
        cont+=1

    if(pri<=2):
        return True
    else:
        return False 

#Implementamos un for para evalauar los numeros del 1 al 1000 y ver cuantos primos hay para sumarlos
for i in range(1,1001):
    bandera = es_primo(i)
    if(bandera):
        sum +=i #si es primo...se suma
        # print(i," es primo\n")

print("La suma de los primos del 1 al 1000 es: "+ str(sum)) #mostramos la suma de los nros primos del 1 al 1000

