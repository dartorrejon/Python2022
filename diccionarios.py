
#Inicializamos el diccionario
agenda = {
            "Nombre": "Dario", 
            "Edad":38,
            "Direccion":"Peru 222",
            "Provincia":"Cordoba"
         }

#Imprimimos el diccionario
print(agenda)

#imprimimos solo las claves con el metodo keys()
for x in agenda.keys():
    print(x)

#Imprimimos solo los valores con el metodo values()
for x in agenda.values():
    print(x)

#Imprimimos claves y valores con el metodo items()
for x ,y in agenda.items():
    print(x,"->",y)

#Tambien se puede usar las funciones in y not in
if "carlos" not in agenda.keys():
    print("si")
else: print("no")

dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

