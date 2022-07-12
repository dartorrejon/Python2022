'''
Escenario
Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario.
 Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

La maquina (por ejemplo, el programa) jugará utilizando las 'X's.
El usuario (por ejemplo, tu) jugarás utilizando las 'O's.
El primer movimiento es de la maquina: siempre coloca una 'X' en el centro del tablero.
Todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia).
El usuario ingresa su movimiento introduciendo el número de cuadro elegido. El número debe de ser valido, 
por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado.
El programa verifica si el juego ha terminado. Existen cuatro posibles veredictos: el juego continua, 
el juego termina en empate, tu ganas, o la maquina gana.
La maquina responde con su movimiento y se verifica el estado del juego.
No se debe implementar algún tipo de inteligencia artificial, la maquina elegirá un cuadro de
 manera aleatoria, eso es suficiente para este juego.

Requerimientos
Implementa las siguientes características:

El tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra
 lista de tres elementos (la lista interna representa las filas) de manera que todos los cuadros puedas 
 ser accedidos empleado la siguiente sintaxis:

board[row][column]


Cada uno de los elementos internos de la lista puede contener 'O', 'X', o un digito representando el número 
del cuadro (dicho cuadro se considera como libre).
La apariencia de tablero debe de ser igual a la presentada en el ejemplo.
Implementa las funciones definidas para ti en el editor.

Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python denominada
 randrange(). El siguiente ejemplo muestra como utilizarla (El programa imprime 10 números aleatorios 
 del 1 al 8).

Nota: La instrucción from-import provee acceso a la función randrange definida en un módulo externo de
 Python denominado random.'''
from random import randrange

tateti = [[1,2,3], [4,"X",6], [7,8,9]]
turno = False

#Definimos las funciones
def DisplayBoard(board):
    print("+---------------+---------------+---------------+")
    for i in range(3):
        print("|\t\t|\t\t|","\t\t|")
        print("|\t",board[i][0],"\t|\t",board[i][1],"\t|\t",board[i][2],"\t|")
        print("|\t\t|\t\t|","\t\t|")
        print("+---------------+---------------+---------------+")


def EnterMove(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    flag = False
    entrada = int(input("Ingrese el cuadro donde ingresar la O [1 a 9]"))

    #Valido que la entrada sea un numero entre 1 y 9
    while entrada < 1 or entrada > 9:
        print("Valor incorrecto!!")
        entrada = int(input("Ingrese el cuadro donde ingresar la O [1 a 9]"))
        
    #Agregamos el O si la posicion esta desocupada
    for i in range(3):
        for k in range(3):
            if board[i][k] == entrada:
                board[i][k] = "O"
                flag = True
                break

    #Si la ubicacion esta ocupada lo mostramos por pantalla
    if not flag:
        print("Lugar ocupado!")
        input("Presione ENTER para continuar....")
                


def MakeListOfFreeFields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    vacios = []
    for i in range(3):
        for k in range(3):
            if type(board[i][k]) == int:
                vacios.append((i,k))
    return vacios

def VictoryFor(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    win = False
    cont = 0
   
   #Comprobamos la diagonal principal
    for i in range(3):
        if board[i][i] == sign:
            cont += 1
    if cont == 3:
        win = True
        return win
    else: cont = 0

    #Comprobamos las filas
    for i in range(3):
        for k in range(3):
            if board[i][k] == sign:
                cont += 1
        if cont == 3: 
            win = True
            return win
        else: cont = 0
    
    #Comprobamos las columnas
    for i in range(3):
        for k in range(3):
            if board[k][i] == sign:
                cont += 1
        if cont == 3: 
            win = True
            return win
        else: cont = 0

    #Comprobamos la diagonal secundaria
    for i in range(3):
        if board[i][2-i] == sign:
            cont +=1
    
    if cont == 3: 
            win = True
            return win
    
    return win
        
def DrawMove(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    fil_col = (randrange(3),randrange(3))
    vacios = MakeListOfFreeFields(board)

    while(fil_col not in vacios):
        fil_col = (randrange(3),randrange(3))

    print("Posicion elegida la N°: ",board[fil_col[0]][fil_col[1]])

    board[fil_col[0]][fil_col[1]] = "X"
    print(DisplayBoard(board))
    


print("-"*40)
print("| Bienvenido al juego del TE - TE - TI |")
print("-"*40)

while MakeListOfFreeFields(tateti) != []:
    if turno:
        print("Turno Pc - X")
        DrawMove(tateti)
        turno = False
        if VictoryFor(tateti,"X"):
            break
        input("Presione ENTER para continuar...")
        print("\n"*50)
    else:
        print("Turno Jugador - O")
        DisplayBoard(tateti)
        EnterMove(tateti)
        turno  = True
        if VictoryFor(tateti,"O"):
            break
        print("\n"*50)
        print("Jugador 1 - O")
        DisplayBoard(tateti)
        input("Presione ENTER para continuar...")
        print("\n"*50)

print("\n"*50)
if MakeListOfFreeFields(tateti) == []:
    print("EMPATE!!")
elif VictoryFor(tateti,"X"):
    print("GANADOR Pc!!")
elif VictoryFor(tateti,"O"):
    print("GANADOR Jugador!!")
DisplayBoard(tateti)
print("Have A NiCe dAy =)")
print("Fin del Juego....")