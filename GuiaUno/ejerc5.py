# Dado un arreglo, imprimir los valores máximo y mínimo.

def cargar(vec):
    num = int(input('Ingresa un numero , 0 para terminar la carga'))
    while num != 0 : 
        vec.append(num)
        
        num = int(input('Ingresa un numero , 0 para terminar la carga'))
        
def valueMax(vec):
    maxValue = vec[0]
    for i in range(len(vec)):
        if vec[i] > maxValue : 
            maxValue = vec[i]
    return maxValue

def valueMin(vec):
    minValue = vec[0]
    for i in range(len(vec)):
        if vec[i] < minValue : 
            minValue = vec[i]
    return minValue

def mostrar(vec):
    for i in range(len(vec)):
        print(vec[i] , end=" ")

        
vecP = []
cargar(vecP)
valorMax = valueMax(vecP)
valorMin = valueMin(vecP)

mostrar(vecP)

print(f'Valor maximo {valorMax}')
print(f'Valor minimo {valorMin}')