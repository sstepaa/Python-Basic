# Ingresar un arreglo e imprimirlo. Se da como dato el número de componentes del vector
vector = []

num = int(input('Introduzca un numero de veces que se itere el vector'))
for i in range(num):
    num_1 = int(input('Introduzca un numero'))
    vector.append(num_1)
    
print(f'El vector es {vector}')