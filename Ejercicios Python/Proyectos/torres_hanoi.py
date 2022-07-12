valor = 0
torre1 = []
torre2 = []
torre3 = []

def cargar_t1(cantidad):
    for i in range(0,cantidad):
        torre1.insert(0,(i+1))

print("TOrre1: ",torre1)

def mostrar_torres():
    print("Torre1: ",torre1)
    print("Torre2: ",torre2)
    print("Torre3: ",torre3)
    input()

def tres_mov(t1,t2,t3):
    t3.append(t1[-1])
    del t1[-1]
    mostrar_torres()
    t2.append(t1[-1])
    del t1[-1]
    mostrar_torres()
    t2.append(t3[-1])
    del t3[-1]
    mostrar_torres()
    t3.append(t1[-1])
    del t1[-1]
    mostrar_torres()
    t1.append(t2[-1])
    del t2[-1]
    mostrar_torres()
    t3.append(t2[-1])
    del t2[-1]
    mostrar_torres()
    t3.append(t1[-1])
    del t1[-1]
    mostrar_torres()



def torres_hanoi(discos,to1,to2,to3):
    cargar_t1(discos)
    mov = (2**discos)-1
    cont = 1
    print("Cantidad justa de movimientos: ",mov)
    while len(to3) != discos:
        if cont %2 != 0:
            if to1 != [] and len(to1) %2 != 0:
                tres_mov(to1,to2,to3)
            if to1 != [] and len(to1) %2 == 0:
                tres_mov(to1,to3,to2)
            if to1 == []:
                if len(to2) > len(to3):
                    tres_mov(to2,to1,to3)
            cont +=1
        else:
            if to3 == []:
                to3.append(to1[-1])
                del to1[-1]
                mostrar_torres()
            cont +=1        
            
    
torres_hanoi(4,torre1,torre2,torre3)