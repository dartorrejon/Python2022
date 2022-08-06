class QueueError(IndexError):  # Eligir la clase base para la nueva excepción.
    pass #se pone la palabra reservada pass cuando queres dejar vacio el metodo


class Queue:
    def __init__(self):
        self.__cola = []


    def put(self, elem):
        self.__cola.insert(0,elem)

    def get(self):
        self.__el = ''
        if len(self.__cola) > 0:
            self.__el = self.__cola[-1]
            del self.__cola[-1]
            return self.__el
        else:
            raise QueueError


que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Error de Cola")
