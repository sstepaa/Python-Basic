#Ingresar un arreglo e imprimirlo. Se da como dato el número de componentes del vector.

def cargar(n , vec):
    for i in range(n):
        num = int(input('Ingresa un numero'))
        vec.append(num)
        
def mostrar(vec):
    for i in range(len(vec)):
        print(vec[i] , end=' ')
        
def valueMax(vec) :
    maxValue = vec[0]
    posMax = 0
    i = 0
    while i < len(vec):
        if vec[i] > maxValue:
            maxValue = vec[i]
            posMax = i
            vec.insert(i + 1 , 0)   
        i += 1
    return maxValue , posMax

vector1 = []        
numeroLenVec = int(input('Ingresa el numero que desea tener la longitud del vector'))


cargar(numeroLenVec , vector1)
valueMax(vector1)
mostrar(vector1)