
'''Calculadora de Sangre
Volver a: 11 de May - 17 ...
Desarrollar un programa que permita al usuario ingresar su grupo sanguíneo como un string (cadena)
y devuelva el grupo del que puede recibir sangre y a quien puede donar. Para realizar el programa
se deberá averiguar la tabla de correspondencias entre grupos sanguíneos. Se deben emplear listas
para almacenar los distintos grupos sanguíneos.'''

#Variables
op= 0

grupos_sanguineos=["A+","O+","B+","AB+","A-","O-","B-","AB-"] #Lista de grupos sanguineos

puede_donar = ["A+, AB+","A+", "O+, B+, AB+","B+, AB+"," AB+","A+, A-, AB+, AB-",
"A+, O+, B+, AB+, A-, O-, B-, AB-","B+, B-, AB+, AB-"] 
#Lista de grupos a cuales le puede donar cada grupo sanguineo

le_donan = ["A+, A-, O+, O-","O+, O-","B+, B-, O+, O-","A+, O+, B+, AB+, A-, O-, B-, AB-",
"A-, O-","O-","B-, O-","A-, O-, B-, AB-"] #Lista de posibles donantes para cada grupo sanguineo

#metodo para mostrar los grupos sanguineos solicitados
def mostrar_gsangui(opcion):
    print("GRUPO "+grupos_sanguineos[opcion]+":")
    print("Puede donar "+puede_donar[opcion])
    print("Puede recibir de: "+le_donan[opcion])

#Menu
def menu():
    print("TABLA DE GRUPOS SANGUINEOS")
    print("==============")
    print(grupos_sanguineos[0])
    print(grupos_sanguineos[1])
    print(grupos_sanguineos[2])
    print(grupos_sanguineos[3])
    print(grupos_sanguineos[4])
    print(grupos_sanguineos[5])
    print(grupos_sanguineos[6])
    print(grupos_sanguineos[7])
    print("SALIR")
    print("==============")

    opcion=input("Elija una opcion: ").upper()
    return opcion

op=menu() #Asignamos el valor ingresado por el usuario a la variable op


while op!="SALIR":
    print("\n\n\n")
    if op == grupos_sanguineos[0]:
        print("==================================")
        mostrar_gsangui(0)    
        print("==================================")
    elif op == grupos_sanguineos[1]:
        print("===============================")
        mostrar_gsangui(1)
        print("===============================")
    elif op == grupos_sanguineos[2]:
        print("================================")
        mostrar_gsangui(2)
        print("================================")
    elif op == grupos_sanguineos[3]:
        print("===========================================================")
        mostrar_gsangui(3)
        print("===========================================================")
    elif op == grupos_sanguineos[4]:
        print("================================")
        mostrar_gsangui(4)
        print("================================")
    elif op == grupos_sanguineos[5]:
        print("=======================================================")
        mostrar_gsangui(5)
        print("=======================================================")
    elif op == grupos_sanguineos[6]:
        print("================================")
        mostrar_gsangui(6)
        print("================================")
    elif op == grupos_sanguineos[7]:
        print("=================================")
        mostrar_gsangui(7)
        print("=================================")

    print("\n")
    op=menu()


print("Fin del Programa!! =)")