'''Objetivos
    Familiarizar al estudiante con:

Proyectar y escribir funciones parametrizadas.
Utilizar la instrucción return.
Utilizar las funciones propias del estudiante.

Escenario
Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número 
de días del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser
universal).

La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos
no tienen sentido.

Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LABORATORIO 4.1.3.6).
Puede ser muy útil. Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de
la función; este truco acortará significativamente el código.

Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.'''

def is_year_leap(año):
    if año % 4 != 0: #no divisible entre 4
        return False
    elif año % 4 == 0 and año % 100 != 0: #divisible entre 4 y no entre 100 o 400
        return True
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: #divisible entre 4 y 10 y no entre 400
        return False
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: #divisible entre 4, 100 y 400
    	return True

def days_in_month(year, month):
    meses31 = [1,3,5,7,8,10,12]
    meses30 = [4,6,9,11]
    if month in meses31:
        return 31
    elif month in meses30:
        return 30
    elif month == 2 and is_year_leap(year):
        return 29
    elif month == 2 and not is_year_leap(year):
        return 28
    else: return

test_years = [1900, 2000, 2016, 1987,1983]
test_months = [2, 2, 1, 11,2]   
test_results = [28, 29, 31, 30,28]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end=" ")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")

def pedirPropina(x):
    print("la propina es: $",x)

print("Usted debe dejar propina:")
pedirPropina(100)