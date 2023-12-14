'''
Cargar en un arreglo 10 números pares y en otro arreglo 5 números impares.
a) Mostrar los elementos de cada arreglo.
b) Hallar el máximo del arreglo A.
c) Hallar el mínimo del arreglo B.
d) Obtener un arreglo C con los elementos de A seguidos de los elementos de B.
e) Obtener un arreglo D con los elementos de A multiplicados por 4

'''

def cargar(vec1 , vec2):
    while len(vec1) < 5 or len(vec2) < 2:
        num = int(input('Ingrese un numero'))
        if num % 2 == 0 : 
            vec1.append(num)
        else : 
            vec2.append(num)
            
def mostrar(msg , vec): 
    print('')
    print(msg)
    for i in range(len(vec)):
        print(vec[i] , end= " ")
        
def maximo(vec):
    maximo = vec[0]
    for i in range(len(vec)):
        if vec[i] > maximo : 
            maximo = vec[i]
    return maximo
            
def minimo(vec): 
    minimo = vec[0]
    for i in range(len(vec)):
        if vec[i] < minimo:
            minimo = vec[i]
    return minimo

def mult_4(vec):
    for i in range(len(vec)):
        vec[i] *= 4
        
vec_par = []
vec_impar = []
cargar(vec_par, vec_impar)

valor_maximo_par = maximo(vec_par)
valor_minimo_impar = minimo(vec_impar)
vec_general = vec_par + vec_impar

if len(vec_par) != 0 and len(vec_impar) != 0:
    mostrar('El vector par es ' , vec_par)
    mostrar('El vector impar es ' , vec_impar)
    print(' ')
    print(f'El valor maximo de los numero pares es {valor_maximo_par} y el valor minimo de los numeros impares es {valor_minimo_impar}')
    print(' ')
    print(f'Los vectores sumados es {vec_general}')
    mult_4(vec_par)
    mostrar('El vector par * 4 es ' , vec_par)
else : 
    print('No hay datos para visualizar')
    
    