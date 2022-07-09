board = [[1,2,3],[4,"X",6],[7,8,9]]
fila = 4
col = 4
def DisplayBoard(board):
    print("+---------------+---------------+---------------+")
    for i in range(3):
        print("|               |               |               |")
        print("|\t"+str(board[i][0])+"\t|\t"+str(board[i][1])+"\t|\t"+str(board[i][2])+"\t|")
        print("|               |               |               |")
        print("+---------------+---------------+---------------+")
        

def EnterMove(board):
    
    validar_ingreso()

    if board[fila][col] != "X" and board[fila][col] != "O":
        board[fila][col] = "X"
    else:
        print("Casilla Ocupada!Ingrese una diferente!")
        validar_ingreso()
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    

# def MakeListOfFreeFields(board):
#     # La función examina el tablero y construye una lista de todos los cuadros vacíos.
#     # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.

# def VictoryFor(board, sign):
#     # La función analiza el estatus del tablero para verificar si
#     # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.

# def DrawMove(board):
#     # La función dibuja el movimiento de la máquina y actualiza el tablero.

def validar_ingreso():
    fila = int(input("Ingrese el numero de fila[1 - 2 - 3]: "))
    while fila < 1 or fila > 3:
        fila = int(input("Valos no permitido!Ingrese nro de fila[1 - 2 - 3]"))

    col = int(input("Ingrese el numero de columna[1 - 2 - 3]: "))
    while col < 1 or col > 3:
        col = int(input("Valos no permitido!Ingrese nro de fila[1 - 2 - 3]"))

DisplayBoard(board)