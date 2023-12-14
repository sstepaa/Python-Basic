#Introducir un arreglo de 10 elementos. Eliminar la primera componente y mostrar elarreglo
vector_A = []
i = 0
#Cargamos el vector desde un while hasta un len de 10
while len(vector_A) < 10 : 
    num = int(input('Introducí un número por favor'))
    vector_A.append(num)
    i += 1
#Imprimimos para verificar si el vector se completo con exitos!
print(f'El vector A completo')
#Con la funcion POP eliminamos la primera posicion del vector como se pide en el enunciado.
vector_A.pop(0)
#Recorremos el vector en sí
for i in vector_A:
    print(i)

print(f'El vector A con la primera posicion elimina es {vector_A}')
    