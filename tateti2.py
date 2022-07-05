board = [[1,2,3],[4,"X",6],[7,8,9]]

def DisplayBoard(board):
    print("+---------------+---------------+---------------+")
    for i in range(3):
        print("|               |               |               |")
        print("|\t"+str(board[i][0])+"\t|\t"+str(board[i][1])+"\t|\t"+str(board[i][2])+"\t|")
        print("|               |               |               |")
        print("+---------------+---------------+---------------+")
        
DisplayBoard(board)
# def EnterMove(board):
#     # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
#     # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.

# def MakeListOfFreeFields(board):
#     # La función examina el tablero y construye una lista de todos los cuadros vacíos.
#     # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.

# def VictoryFor(board, sign):
#     # La función analiza el estatus del tablero para verificar si
#     # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.

# def DrawMove(board):
#     # La función dibuja el movimiento de la máquina y actualiza el tablero.
