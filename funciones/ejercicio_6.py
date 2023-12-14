'''
Ingresar números enteros hasta cargar dos arreglos con 10 valores cada uno, uno con aquellos números impares múltiplos de 3 y otro con aquellos números múltiplos de 6.

Mostrar dichos arreglos.
Intercalar de forma ordenada dichos arreglos formando un solo arreglo. El arreglo resultante de la intercalación debe estar ordenado en forma descendente.
Eliminar de este nuevo arreglo los números impares negativos.
'''

def carga(vec1 , vec2):
    while len(vec1) != 3 or len(vec2) != 3:
        num = int(input('Ingresa un numero'))
        if num % 2 == 1 and num % 3 == 0:
            vec1.append(num)
        if num % 6 == 0:
            vec2.append(num)
            
def intercalar(vec1 ,vec2):
    vec_t = []
    i = 0
    j = 0
    
    while i < len(vec1) and j < len(vec2):
        vec_t.append(vec1[i])
        vec_t.append(vec2[i])
        
        i+=1
        j+=1
    #Agregar cualquier elemento restante del vector vec1
    while i < len(vec1):
        vec_t.append(vec1[i])
        
        i+= 1
    #Agregar cualquier elemento restante del vector vec2
    while i < len(vec2):
        vec_t.append(vec2[j])
        
        j += 1
    return vec_t

def eliminar(vec):
    i = 0
    while i < len(vec):
        if vec[i] < 0 and vec[i] % 2 == 1:
            vec.pop(i)
        else:
            i += 1
    return vec

def mostrar(msg, vec1,vec2):
        print(' ')
        print(msg)
        for i in range(len(vec1)):
            print(f'{vec1[i]}\t{vec2[i]}')
vec_a = []
vec_b = []
carga(vec_a , vec_b)
if len(vec_a) != 0 and len(vec_b) != 0:
    mostrar('Los vectores son :' , vec_a , vec_b)
    vector_intercalado = intercalar(vec_a , vec_b)
    print(f'vector intercalado es {vector_intercalado}')
    vector_elim = eliminar(vector_intercalado)
    print(f'Vector con elementos eliminados {vector_elim}')   
else : 
    print('No hay datos') 
    
    
