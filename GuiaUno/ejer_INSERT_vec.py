vec = []
#Bloque que carga el vector
for i in range(4):
    num = int(input('Ingrese un numero : '))
    vec.append(num)
#Bloque que carga el vector

print('Datos cargados : ')
#Bloque que recorre el vector y muestra cada elemento
for i in range(len(vec)):
    print(vec[i] , end=" ")
print(f'El largo del vector es : {len(vec)}')
#Bloque que recorre el vector y muestra cada elemento

#El ciclo se va a ejecutar MIENTRAS que la variable de control(I) sea menor a la cantidad de elementos que tiene el vec.
i = 0 
while i < len(vec):
    if vec[i] % 2 != 0:
        vec.insert(i + 1 , 0)
    i += 1
#El ciclo se va a ejecutar MIENTRAS que la variable de control(I) sea menor a la cantidad de elementos que tiene el vec. 
# [i+ 1] posicion continua de indice.
# La insercion de un elemento en el vector va a ser por naturaleza que se modifique el LEN(vec) , esto afecta de manera directa en el range(len(vec)) del for , por que no se actualiza, queda con el len viejo.
    
print("Datos despues de insertar: ")
for i in range(len(vec)):
    print(vec[i] , end=" ")
print(f'El largo del vector es : {len(vec)}')