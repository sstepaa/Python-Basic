#MAXIMO Y MINIMO dentro de un vector
vector = [7,6,5,9,10,1]

valor_minimo = vector[0]
valor_maximo = vector[0]

for i in range(len(vector)):
    if valor_minimo > vector[i]:
        valor_minimo = vector[i]
    
    if valor_maximo < vector[i]:
        valor_maximo = vector[i]
print(f'El valor minimo del vector es el {valor_minimo}')
print(f'El valor maximo del vector es el {valor_maximo}')