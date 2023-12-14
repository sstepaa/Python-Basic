'''
Se desea cargar un arreglo con los números positivos y otro arreglo con los numero negativo leídos, 
la carga de datos finaliza al leer un cero. 
Indicar el valor mínimo de los positivos y el máximo de los negativos y luego intercambiarlos
'''

vector_P = []
vector_N = []

#Estamos haciendo la carga de dos vectores distintos uno de + y - en una sola funcion
#Nos ahorra el paso previo de hacer un vector madre , recorrerlo y hacer dos vectores de un mismo vector.
def carga(vec_positivo , vec_negativo):#Paso como paremetros los dos vectores 
    num = int(input('Introduci un numero'))
    while num != 0 : 
        if num > 0 : 
            vec_positivo.append(num)
        else:
            vec_negativo.append(num)
        
        num = int(input('Introduci un numero'))


def minimo(vec):
    pos = vec[0] 
    for i in range(len(vec)):
        if vec[i] < pos : 
            pos = vec[i]
        return pos
def maximo(vec):
    pos = vec[0]
    for i in range(len(vec)):
        if vec[i] > pos : 
            pos = vec[i]
        return pos
    
def intercambio(positivo , negativo , maxi , mini):
    aux = negativo[maxi]
    negativo[maxi] = positivo[mini]
    positivo[mini] = aux
    
def mostrar(vector , msg):
    print(' ')
    print(msg)
    for i in range(len(vector)):
        print(vector[i] , end=" ")
    
carga(vector_P , vector_N)
if len(vector_P) != 0 and len(vector_N) != 0:
    mostrar(vector_P , 'Positivos')
    mostrar(vector_N , 'Negativos')
    minimo = minimo(vector_P)
    maximo = maximo(vector_N)
    print(f'El mayor de los negativos es {maximo}')
    print(f'El menor de los positivos es {minimo}')
    intercambio(vector_P,vector_N,maximo,minimo)
    mostrar(vector_P , 'Positivos despues del cambio')
    mostrar(vector_N , 'Negativos despues del cambio')
else:
    print('No hay datos para mostrar')