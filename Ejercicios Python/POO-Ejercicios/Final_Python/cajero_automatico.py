'''Desarrollar un programa que emule un ATM (cajero automático). Al inicio el 
programa debe solicitar una clave numérica de cuatro dígitos para ingresar a la cuenta, en 
caso de no coincidir con ninguna cuenta existente devolver un mensaje y volver a pedir una 
clave. El programa debe tener precargada las cuentas de tres personas en un diccionario.
En caso de que se ingrese una clave existente el programa debe solicitar que acción
desea realizar. Para ello se cuenta con un menú:
 1 ….. Ingresar Dinero
 2 ….. Retirar Dinero
 3 ….. Cambiar contraseña 
 4 ….. Solicitar préstamo
 5 …. Consultar Saldo
 6 ….. Salir
Cada persona dispone de su cuenta por lo que el programa deberá llevar el saldo 
disponible en forma independiente.
Al finalizar una operación el programa pregunta si desea realizar otra operación o 
salir.
El programa debe ser realizado en base al paradigma procedimental, debiendo estar 
correctamente documentado'''
#Diccionario con los clientes
clientes = {"Dario" : [1234,56864.87], "Maria" : [4325,15000.0] , "Pablo": [6345,9450.23]}
clave = 0
usuario = []
opcion = 0

#Limpia la pantalla
def limpiar_pantalla():
    print("\n"*50)

#Mensaje de Bienvenida     
def bienvenida():
    print("-"*41)
    print("| Bienvenido/a al cajero de RED BANELCO |")
    print("-"*41)

#Menu de bienvenida
def menu1(nombre,op):
    global opcion
    opcion = op
    limpiar_pantalla()
    bienvenida()
    print("Usuario/a "+nombre.upper()+": ")
    print(''' 1 - Ingresar Dinero
 2 - Retirar Dinero
 3 - Cambiar contraseña 
 4 - Solicitar préstamo
 5 - Consultar Saldo
 6 - Salir''')
    opcion = int(input("Elija una opcion: "))
    while opcion <1 or opcion >6:
        print("Opcion incorrecta!")
        menu2()
        opcion= int(input("Elija una opcion: "))

#Menu2
def menu2():
    print(''' 1 - Ingresar Dinero
 2 - Retirar Dinero
 3 - Cambiar contraseña 
 4 - Solicitar prestamo
 5 - Consultar Saldo
 6 - Salir''')

#Opcion 1:Ingresa dinero a la cuenta
def op1(nombre,cant):
    clientes[nombre][1] += cant

#Opcion 2: Retira dinero de la cuenta si fuera posible
def op2(nombre,cant):
    if clientes[nombre][1]>=cant:
        clientes[nombre][1] -= cant
        print("Usted acaba de retirar $ "+cant)
        print("Salto remanente $ "+clientes[nombre][1])
    else:
        print("Saldo insuficiente!")

#Opcion 3: Cambiar contraseña
def op3(nombre, nueva_pass):
    nueva_pass = val_entrada(nueva_pass)
    clientes[nombre][0] = nueva_pass
    print("Clave modificada!")

#Opcion 4: Solicitar Prestamo
def op4(nombre):
    if clientes[nombre][1] == 0:
        cantidad = 10000
    elif clientes[nombre][1] > 0 and clientes[nombre][1] < 50000:
        cantidad = 30000
    elif clientes[nombre][1] >= 50000 and clientes[nombre][1] <= 100000:
        cantidad = 75000
    elif clientes[nombre][1] >100000:
        cantidad = 100000
    prestamo = float(input("Ingrese la cantidad que desea solicitar[Max = $"+str(cantidad)+"]: "))
    while(prestamo < 0 or prestamo > cantidad):
        print("Ingreso una cantidad no permitida!!")
        prestamo = float(input("Ingrese la cantidad que desea solicitar[Max = $"+str(cantidad)+"]: "))
    
    clientes[nombre][1] +=prestamo
    print("Prestamo otorgado!")
    print("Saldo actualizado $ "+str(clientes[nombre][1]))
    
#Opcion 5: Consultar Saldo
def op5(nombre):
    return clientes[nombre][1]       

#Valida la entrada de la clave
def val_entrada(ent):
    while(ent <1000 or ent >9999):
        print("Clave no valida!")
        ent = int(input("Ingrese su clave de 4 digitos por favor: "))
    return ent
    

#Verifica que la clave este en la base de datos
def verifica_clave(cl_pass):
    for x,y in clientes.items():
        if cl_pass == y[0]:
            usuario = [x,cl_pass]
            return usuario
            
#Programa principal
def main():
    intentos=0
    global clave
    bienvenida()
    try:
        clave = val_entrada(int(input("Ingrese su clave de 4 digitos por favor: ")))
     
        while(verifica_clave(clave) == None):
            print("Clave inexistente!!",4-intentos,"intentos restantes: ")
            intentos += 1
            if intentos ==5:
                print("Supero la cantidad de intentos!!")
                print("Vuelva a intentarlo mas tarde o pongase en contacto con el Banco")
                print("Fin del Programa...")
                break
            clave = val_entrada(int(input("Ingrese una nueva clave por favor: ")))
        
        
        if intentos <=4:
            usuario = verifica_clave(clave)
            menu1(usuario[0],opcion)
            if opcion == 5:
                limpiar_pantalla()
                print("Usuario "+usuario[0].upper()+": ")
                print("Su saldo actual es $",op5(usuario[0]))
            elif opcion == 4:
                op4(usuario[0])

    except ValueError:
        print("Solo se aceptan numeros!")
        print("Fin del Programa....")
main()


