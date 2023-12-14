#Dado un arreglo, imprimir los valores máximo y mínimo.
vector_Stepa = [2,4,6,8,4,6,7]

max_vector = vector_Stepa[0]
min_vector = vector_Stepa[0]

for i in range(len(vector_Stepa)):
    if min_vector > vector_Stepa[i]:
        min_vector = vector_Stepa[i]
    if max_vector < vector_Stepa[i]:
        max_vector = vector_Stepa[i]

print(f'El minimo elemento del vector es {min_vector}')
print(f'El maximo elemento del vector es {max_vector}')