fila = 0
col = 0
tateti = [[" " for i in range(3)]for j in range(3)]
gano1 = False
gano2 = False
emp = False
turnos = 0
def mostrar_tateti():
    for i in tateti:
        print(i)

def agregar_valor(fil,col,val):
    if tateti[fil-1][col-1] == " ":
        tateti[fil-1][col-1] = val
    else:
        print("Lugar ocupado!!")

def comprobar_diagonal_principal(val):
    cont = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                if tateti[i][j] == val:
                    cont += 1
    
    if cont == 3: return True
    else: return False

def comp_diag_secu(val):
    col = 2
    cont = 0
    for i in range(3):
        if tateti[i][col] == val:
            cont += 1
        col -= 1
    
    if cont == 3: return True
    else: return False
    
def comp_filas(val):
    cont = 0
    for fil in tateti:
        for col in fil:
            if col == val:
                cont += 1
        if cont == 3: break
        else: cont = 0
    
    if cont == 3: return True
    else: return False

def comp_colums(val):
    cont = 0
    for i in range(3):
        for j in range(3):
            if tateti[j][i] == val:
                cont += 1
        if cont == 3: break
        else: cont = 0
    
    if cont == 3: return True
    else: return False

def comp_tateti(val):
    return (comp_colums(val) or comp_diag_secu(val) or comp_filas(val) or comprobar_diagonal_principal(val))

def empate():
    ban = False
    for fil in tateti:
        for col in fil:
            if " " not in col:
                ban = True
            else: ban = False
    return ban

while not gano1 and not gano2 and not emp:
    if turnos %2 == 0:
        print("Turno Jugador 1[X]: ")
        fila =int(input("Ingrese la fila[1 - 2- 3]: "))
        col = int(input("Ingrese la columna[1 - 2- 3]: "))
        agregar_valor(fila,col,"X")
        mostrar_tateti()
        if turnos >= 3:
            if comp_tateti("X"):
                gano1 = True
    elif turnos % 2:
        print("Turno Jugador 2[O]: ")
        fila =int(input("Ingrese la fila[1 - 2- 3]: "))
        col = int(input("Ingrese la columna[1 - 2- 3]: "))
        agregar_valor(fila,col,"O")
        mostrar_tateti()
        if turnos >= 3:
            if comp_tateti("O"):
                gano2 = True
    if turnos >=7:
        emp = empate()
    turnos += 1

if gano1: print("Ganador Jugador 1!!")
elif gano2: print("Ganador Jugador 2!!!")
elif emp: print("Empate!!")
    
 
    

  


