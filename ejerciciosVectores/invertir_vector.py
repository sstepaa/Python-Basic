vectorS = [2 ,3 , 5 , 3 , 2 , 4 , 5 , 7 , 8 , 9 ]
for i in range(len(vectorS) // 2):
    var_aux = vectorS[i]
    vectorS[i] = len(vectorS) - 1 - i
    vectorS[len(vectorS) - 1 - i] = var_aux
print(vectorS)
#Reveer