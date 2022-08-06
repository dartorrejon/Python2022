class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__contador = 0

    def get_counter(self):
        return self.__contador
    
    def push(self, val):
        Stack.push(self, val)
        self.__contador +=1

    def pop(self):
        self.__contador += 1
        Stack.pop(self)
	

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print("Cantidad de elementos agragados y eliminados:",stk.get_counter())