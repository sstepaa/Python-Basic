#Ingresar un arreglo de 10 componentes:
# a. Imprimir la cuarta componente.
# b. Imprimir las componentes en orden invertida.
# c. Imprimir el producto entre la primera y la última componente.
# d. Imprimir las componentes de índice impar.
# e. Imprimir la suma de las componentes de índice par.
# f. Imprimir la multiplicación de las componentes de índice impar.
# g. Imprimir el arreglo que resulta de intercambiar la primera con la últimacomponente

def carga(n , vec):
    for i in range(n):
        num = int(input('Ingresa un numero'))
        vec.append(num)
        
def mostrar(vec):
    for i in range(len(vec)):
        print(vec[i] , end=" ")

def invertirVector(vec):
    #MetodoBurbuja
    for i in range(0 , len(vec) -1 , 1):
        for j in range(i + 1 , len(vec) , 1):
            if vec[i] < vec[j]: 
                aux = vec[i]
                vec[i] = vec[j]
                vec[j] = aux

def indexPar(vec):
    vecSeg = []
    sumPar = 0
    for i in range(len(vec)):
        if vec[i] % 2 == 0 :
            vecSeg.append(vec[i])
            sumPar += vec[i]
    return vecSeg , sumPar

def indexImpar(vec):
    mulpImpar = 1
    for i in range(len(vec)):
        if vec[i] % 2 == 1 : 
            mulpImpar *= vec[i]
            
    return mulpImpar

def vectorIntercambio(vec):
    for i in range(len(vec)):
        aux = vec[0]
        vec[0] = vec[-1]
        vec[-1] = aux    
        
#Programa general 
vec1 = []

numVec = int(input('ingresa el numero de longitud del vector'))
carga(numVec , vec1)
mostrar(vec1)
if len(vec1) >= 4:
    print(f'El vector es la posicion 4 es {vec1[3]}')
else : 
    print('El vector no es lo suficientemente extenso')

invertirVector(vec1)
paresVec , SumVecPar = indexPar(vec1)

if len(paresVec) == 0 :
    print('No hay datos para mostrar')
else : 
    print(f'El vector con numeros pares es {paresVec} y la suma de ellos es {SumVecPar}')
