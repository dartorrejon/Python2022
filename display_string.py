'''Objetivos
Mejorar las habilidades del alumno al trabajar con cadenas.
Usar cadenas para representar datos que no son texto.
Escenario
Seguramente has visto un display de siete segmentos.

Es un dispositivo (a veces electrónico, a veces mecánico) diseñado para presentar un dígito decimal 
utilizando un subconjunto de siete segmentos. Si aún no sabes lo qué es, consulta la siguiente liga
 en Wikipedia: https://en.wikipedia.org/wiki/Seven-segment_display.

Tu tarea es escribir un programa que puede simular el funcionamiento de un display de siete segmentos,
 aunque vas a usar LEDs individuales en lugar de segmentos.

Cada dígito es construido con 13 LEDs (algunos iluminados, otros apagados, por supuesto), así es como
 lo imaginamos:'''

#Guardamos en listas las diferentes lineas para imprimir en el display
lin1 = ["###","  #","###","###","# #","###","###","###","###","###"]
lin2 = ["# #","  #","  #","  #","# #","#  ","#  ","  #","# #","# #"]
lin3 = ["# #","  #","###","###","###","###","###","  #","###","###"]
lin4 = ["# #","  #","#  ","  #","  #","  #","# #","  #","# #","  #"]
lin5 = ["###","  #","###","###","  #","###","###","  #","###","###"]

#Entrada y validacion del valor
valor = int(input("Ingrese un numero entero positivo: "))
while valor < 0:
    print("Valor negativo no aceptado!!!")
    valor = int(input("Ingrese un numero entero positivo: "))
valor = str(valor)

#Imprimimos linea por linea en el Display
for char in valor:
     print(lin1[int(char)],end=' ')
print()
for char in valor:
     print(lin2[int(char)],end=' ')
print()
for char in valor:
     print(lin3[int(char)],end=' ')
print()
for char in valor:
     print(lin4[int(char)],end=' ')
print()
for char in valor:
     print(lin5[int(char)],end=' ')
