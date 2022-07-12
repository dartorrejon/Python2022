from random import *

intentos = 0 #nro de intentos
pal_completa = False #bandera para ver cuando la palabra este completa

#Lista de palabras
palabras = ['otorrinolaringologo','hipertexto','souvenir','hipervinculo','fortaleza','fluorecente','telgopor',
'diversidad','canones','motricidad','hexadecimal','portaretrato','palindromo','anexado','bilirrubina','filantropo'] 
palabra_aleatoria = palabras[randint(0,len(palabras)-1)] #Guardamos una palabra al azar
pal_aleatoria = list(palabra_aleatoria) # transformamos en LISTA a la palabra aleatoria
pal_ale_aux = pal_aleatoria[:]
opcion = 0
palabra2=""

#Cargamos con _ la lista auxiliar de palabra
for j in range (0,len(pal_ale_aux)):
    pal_ale_aux[j] = "_"

#Funcion que dibuja al ahoracado
def dibujar_ahorcado(intento):
    if intento == 1:
        print("""
                 ------
                 |    ||
                 O    ||
                      ||
                      ||
                      ||
                      ||
                 =========== """)
    elif intento == 2:
       print("""
                 ------
                 |    ||
                 O    ||
                /     ||
                      ||
                      ||
                      ||
                 =========== """)
    elif intento == 3:
        print("""
                 ------
                 |    ||
                 O    ||
                / \   ||
                      ||
                      ||
                      ||
                 =========== """)
    elif intento == 4:
        print("""
                ------
                 |    ||
                 O    ||
                /|\   ||
                      ||
                      ||
                      ||
                 =========== """)
    elif intento == 5:
        print("""
                 ------
                 |    ||
                 O    ||
                /|\   ||    
                /     ||
                      ||
                      ||
                 =========== """)
    elif intento == 0:
        print("""
                 ------
                 |    ||
                      ||
                      ||
                      ||
                      ||
                      ||
                 =========== """)
    elif intento == 6:
         print("""
                 ------
                 |    ||
                \U0001F641    ||
                /|\   ||    
                / \   ||
                      ||
                      ||
                 =========== """)
    elif intento == 7:
        print("""   
                  ------
                 |    ||
                      ||
                      ||
                      ||    
                      ||       \U0001F600  
                      ||       /|\       
                 ===========   / \  """)

#Funcion para limpiar la pantalla
def cls():
    print("\n"*50)

print("==========================================")
print("Bienvenido al Juego del ahorcado!!\nTiene 5 intentos para adivinar la palabra!")
print("Su palabra consta de ",len(pal_aleatoria)," letras!!")
print("¿Podra salvarlo? A JUGAR!!")
print("==========================================")

dibujar_ahorcado(intentos)
print(pal_ale_aux)
letra = input("Ingrese una letra("+str(intentos)+" intento de 5): ")
cls()
while (not pal_completa) and intentos <=5:
    
    for i in range(0,len(pal_aleatoria)):
        if letra == pal_aleatoria[i]:
            pal_ale_aux[i] = letra

    if "_" not in pal_ale_aux:
        pal_completa = True
        break

    if letra not in pal_aleatoria:
        intentos +=1   

    dibujar_ahorcado(intentos)
    print(pal_ale_aux)
    
    if intentos > 3 and intentos < 6:
        print("=============================================================")
        print("("+str(intentos)+" intentos de 5).Desea arriesgar una palabra?![1- SI 2- NO]")
        print("=============================================================")
        opcion=input()
        if opcion == "1":
            palabra2 = input("Ingrese la palabra: ")
            
            if palabra_aleatoria == palabra2.lower():
                pal_completa = True
            else:
                print("Error!!Palabra equivocada!! =(")
                intentos = 6
        else:
            letra = input("Ingrese una letra: ("+str(intentos)+" intento de 5): ")
    elif intentos <= 3:
        letra = input("Ingrese una letra: ("+str(intentos)+" intento de 5): ")
    cls()

if pal_completa == True:
    dibujar_ahorcado(7)
    print("Felicidades Gano el juego del Ahoracado! La palabra era "+palabra_aleatoria.upper())
else:
    dibujar_ahorcado(6)
    print(pal_ale_aux)
    print("Perdio!Lo sentimos vuelva a Interntarlo!! =(")

print("Fin del programa....")



