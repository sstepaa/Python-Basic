'''
Leer números hasta cargar un arreglo de 10 componentes con los números pares.
a) Mostrarlo.
b) Generar otro arreglo con los elementos que están ubicados entre las posiciones del máximo y del mínimo.
Si el máximo y el mínimo están juntos, mostrar “no existe el arreglo”

'''

def cargar(vec):
    while len(vec) < 4 : 
        num = int(input('Ingresa un numero'))
        if num % 2 == 0:
            vec.append(num)
            
def maximo(vec):
    maximo = vec[0]
    for i in range(len(vec)):
        if maximo > vec[i]:
            maximo = vec[i]
    return maximo

def minimo(vec):
    minimo = vec[0]
    for i in range(len(vec)):
        if minimo < vec[i]:
            minimo = vec[i]
    return minimo

def mostrar(msg , vec):
    print(' ')
    print(msg)
    for i in range(len(vec)):
        print(vec[i] , end= ' ')
        
vector_A = []
cargar(vector_A)

if len(vector_A) != 0 :
    mostrar('El vector A es ' , vector_A)
else : 
    print('No hay datos para mostrar')