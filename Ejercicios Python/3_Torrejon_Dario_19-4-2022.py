'''Desarrollar un algoritmo que permita determinar el signo del zodiaco del usuario. Deberán determinar la información necesaria, 
la cual proveera el usuario para poder devolver el resultado como una cadena de texto. El estudiante deberá previamente recolectar 
la información necesaria para que el programa pueda determinar correctamente lo requerido.'''

'''Ingresan al programa 2 valores, el dia y el mes de nacimiento(Se utiliza la funcion upper() para pasar
todas las letras a mayusculas). Luego de eso utilizamos tambien una variable boolean como bandera para 
validar la fecha. Verificamos que el dia sea un digito y luego verificamos que el nombre del mes sea
 el correcto. Si hay algun error en cualquiera de los 2 ingresos se informa y se termina
el programa. Si esta todo bien se pasa a verificar las fechas para mostrar por pantalla el signo 
correspondiente a la fecha del nacimiento; terminando con un saludo al final del programa =)'''

#Variables
dia = input("Ingrese su dia de nacimiento: ")
mes = input("Ingrese el mes de su nacimiento: ").upper()
#pasamos todas las letras a mayusculas con la funcion upper().
bandera = False

#Verificamos que la entrada este bien 
if dia.isdigit():
    dia = int(dia) #Convertimos a entero el dia para poder operar con el valor
    #Meses con 31 dias
    if(dia >= 1 and dia <= 31) and (mes == "ENERO" or mes == "MARZO" or mes == "MAYO" or mes == "JULIO" or mes == "AGOSTO" or mes == "OCTUBRE" or mes == "DICIEMBRE"):
        bandera = True
        #Meses con 30 dias
    elif(dia >=1 and dia <=30) and (mes == "ABRIL" or mes == "JUNIO" or mes == "SEPTIEMBRE" or mes == "NOVIEMBRE"):
            bandera = True
            #Febrero           
    elif(dia >=1 and dia <=29) and mes == "FEBRERO":
                bandera = True
    else:
        print("Error en la fecha ingresada!")
    
else:
    print("El dia ingresado NO ES UN NUMERO!")


#AVERIGUAMOS EL SIGNO SEGUN LA FECHA DE NACIMIENTO
if(bandera and ((dia>=21 and mes == "MARZO") or (dia<=20 and mes == "ABRIL"))):
    print("-------------------------")
    print("Usted es del signo ARIES")
    print("-------------------------")
elif (bandera and ((dia>=21 and mes == "ABRIL") or (dia<=20 and mes == "MAYO"))):
    print("-------------------------")
    print("Usted es del signo TAURO")
    print("-------------------------")
elif (bandera and ((dia>=21 and mes == "MAYO") or (dia<=21 and mes == "JUNIO"))):
    print("--------------------------")
    print("Usted es del signo GEMINIS")
    print("--------------------------")
elif (bandera and ((dia>=22 and mes == "JUNIO") or (dia<=21 and mes == "JULIO"))):
    print("-------------------------")
    print("Usted es del signo CANCER")
    print("-------------------------")
elif (bandera and ((dia>=22 and mes == "JULIO") or (dia<=23 and mes == "AGOSTO"))):
    print("----------------------")
    print("Usted es del signo LEO")
    print("----------------------")
elif (bandera and ((dia>=24 and mes == "AGOSTO") or (dia<=23 and mes == "SEPTIEMBRE"))):
    print("------------------------")
    print("Usted es del signo VIRGO")
    print("------------------------")
elif (bandera and ((dia>=24 and mes == "SEPTIEMBRE") or (dia<=23 and mes == "OCTUBRE"))):
    print("------------------------")
    print("Usted es del signo LIBRA")
    print("------------------------")
elif (bandera and ((dia>=24 and mes == "OCTUBRE") or (dia<=22 and mes == "NOVIEMBRE"))):
    print("---------------------------")
    print("Usted es del signo ESCORPIO")
    print("---------------------------")
elif (bandera and ((dia>=23 and mes == "NOVIEMBRE") or (dia<=21 and mes == "DICIEMBRE"))):
    print("----------------------------")
    print("Usted es del signo SAGITARIO")
    print("----------------------------")
elif (bandera and ((dia>=22 and mes == "DICIEMBRE") or (dia<=20 and mes == "ENERO"))):
    print("------------------------------")
    print("Usted es del signo CAPRICORNIO")
    print("------------------------------")
elif (bandera and ((dia>=21 and mes == "ENERO") or (dia<=19 and mes == "FEBRERO"))):
    print("--------------------------")
    print("Usted es del signo ACUARIO")
    print("--------------------------")
elif (bandera and ((dia>=20 and mes == "FEBRERO") or (dia<=20 and mes == "MARZO"))):
    print("-------------------------")
    print("Usted es del signo PISCIS")
    print("-------------------------")


print("Fin del Programa\nHave a Nice Day! =)")



    
