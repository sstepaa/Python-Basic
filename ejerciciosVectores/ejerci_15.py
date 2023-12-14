'''
Leer 15 números y generar un arreglo con los primeros 8 números mayores que 20.
Si no hay 8 números que cumplan la condición, repetir el primero hasta completar el arreglo.
Si ningún número era mayor que 20, mostrar mensaje y salir.

a.Calcular el promedio de los números que no entraron en el arreglo.
b.Buscar el máximo elemento y mostrar el elemento que esté en la posición anterior.
c.Mostrar el factorial de los elementos de posición par del arreglo
'''
vector_X = []
vector_A = []

acum_menor = 0
cont_menor = 0


for i in range(5): 
    num = int(input('Ingrese un numero'))
    vector_X.append(num)
            
max_elemento = vector_X[0]

i = 0
while i < len(vector_X) and len(vector_A) < 3:
    if  vector_X[i] >= 20: 
        vector_A.append(vector_X[i])  
    else : 
        acum_menor += vector_X[i]
        cont_menor += 1
        
    if vector_X[i] > max_elemento:
        max_elemento = vector_X[i - 1]
        
    i += 1

if len(vector_A) < 1:
    print('No hay nigun numero mayor a 20')
else : 
    while len(vector_A) != 3:
        vector_A.append(vector_A[-1])
    print(f'El vector original es {vector_X}')
    print(f'Y su vector con los numeros mayores a 20 es {vector_A}')

if cont_menor == 0 or acum_menor == 0:
    print(f'No se puede realizar el promedio por falta de datos')
else: 
    print(f'El promedio de los numeros menores a 20 es {acum_menor/ cont_menor}')

print(f'El elemento anterior al valor maximo es {max_elemento} ')