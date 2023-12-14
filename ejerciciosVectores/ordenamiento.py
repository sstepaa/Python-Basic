vectorS = [2 ,3 , 5 , 3 , 2 , 4 , 5 , 7 , 8 , 9 ]
#Metodo de burbuja
#Me paro en el valor 0 de el vector y lo uso de pivot 
#pivot +1 
#Variable auxiliar

for pivot in range(len(vectorS) - 1):
    for pivot1 in range(pivot + 1 , len(vectorS)):
        if vectorS[pivot] > vectorS[pivot1]:
            aux = vectorS[pivot]
            vectorS[pivot] = vectorS[pivot1]
            vectorS[pivot1] = aux
            
print(f'El vector ordenado es {vectorS}')