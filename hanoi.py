torre1 = 1
torre2 = 2
torre3 = 3
n = 3

def hanoi(di, o, d, a):
    if (di == 1):
        print("Mueva el disco ",di," desde la torre ",o," hasta la torre ",d)
    else:
        #Se mueve di-1 de origen a auxiliar
        hanoi(di-1,o,a,d)
        print("Mueva el disco ",di," desde la torre ",o," hasta la torre ",d)

        #Se mueve di-1  de auxiliar a destino
        hanoi(di-1,a,d,o)

hanoi(n,torre1,torre3,torre2)
