# Se carga el arreglo A con 10 números pares y el arreglo B con 10 números múltiplos de5
# a) Generar un arreglo C con los todos los elementos de A y a continuación todos los elementosde B.
# b) Invertir el arreglo A sobre sí mismo.
# c) Buscar la posición del máximo de B.
# Mostrar la posición del máximo y el valor del máximo.
# Poner en cero los valores a la derecha del máximo

def cargar(vecPar , vecInpar):
    num = int(input('Ingresa un numero'))
    
    while len(vecPar) <= 3 or len(vecInpar) <= 3 : #las sentecias revisar
        if num % 2 == 0 :
            vecPar.append(num)
        else : 
            vecInpar.append(num)
            
        num = int(input('Ingresa un numero'))
        
def invertir(vec):
    for i in range(len(vec)//2):
        aux = vec[i]
        vec[i] = len(vec) -1 -i
        vec[len(vec) -1 -i] = aux
        
def valueMax(vec):
    maxValue = vec[0]
    posMax = 0
    i = 0
    while i < len(vec):
        if vec[i] > maxValue:
            maxValue = i
            posMax = vec[i]  
        i += 1
    return maxValue , posMax

vecPar = []
vecImpar = []

cargar(vecPar , vecImpar)

if len(vecPar) == 0 and len(vecImpar) == 0:
    print('No hay datos para mostrar')
else:
    print(vecPar , vecImpar)
    vecC = vecPar + vecImpar
    print(f'vector C : {vecC}')
    invertir(vecPar)
    print(f'Vector Par invertido {vecPar}')
    posMax , maxValue = valueMax(vecImpar)
    vecImpar.insert(posMax + 1 , 0)
    print(f'El valor maximo del vector Impar es {maxValue} , en la posicion {posMax} , vector : {vecImpar}')
    