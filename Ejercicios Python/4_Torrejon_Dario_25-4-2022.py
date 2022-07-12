'''Cúantos viajes me quedan ?
Volver a: 27 de April - 3...
Desarrollar un algoritmo para determinar la cantidad de viajes en colectivo que restan dado un saldo
 inical y una tarifa. El Usuario deberá ingresar su saldo actual y la tarifa por viaje actual,
  luego el programa devolverá como un número entero la cantidad de viajes restantes y el saldo final
   que quedaría en la tarjeta. Si la cantidad de viajes restantes es inferior a 4 viajes el programa
    debe emitir el mensaje "Usted se está por quedar sin pasajes, recuerde recargar su tarjeta". 
    En caso de que de menos de un viaje indicar "No dispone de viajes".'''

#Variables
saldo =float(input("Ingrese su saldo actual $"))
tarifa = float(input("Ingrese la tarifa actual $"))

if(tarifa != 0.0 and int(saldo//tarifa) > 4 and saldo != 0.0):
  #valido primero la tarifa diferente de 0 para evitar la division /0
  print("Le quedan ",int(saldo//tarifa),"viajes.")
  print("Saldo $",round(saldo%tarifa,2)) #Utilizo la funcion round para mostrar solo 2 decimales
elif (tarifa != 0.0 and int(saldo//tarifa) != 0):
#valido primero la tarifa diferente de 0 para evitar la division /0
  print("Usted se está por quedar sin pasajes, recuerde recargar su tarjeta")
else:
  print("No dispone de viajes o ingresaste tarifa $ 0")

print("Fin del programa! =)")

#¿Sería posible que nuestro programa nos envíe un mail automáticamente para recordarnos?, ¿Cómo sería?
'''Si seria posible utilizando una libreria que seguramente ya existe para Python. En orden de hacerlo
a travez de Pseudocodigo redacto los pasos que creo serian necesarios para realizar el envio del mail:
1-Incorporar la libreria para enviar el mail al programa
2-Solicitar al usuario su correo electronico y almacenarla en una variable
3-Validar el formato de la direccion de correo electronico
4-Pasar por parametro la variable que almacena el email a la funcion correspondiente
5-Enviar el email
6-Fin del envio del email'''