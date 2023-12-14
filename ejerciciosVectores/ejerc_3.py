#Dados dos arreglos A y B de N<15 elementos cada uno, calcular un arreglo C tal queC = A + B
vector_a = []
vector_b = []
#Carga el numero de elementos que contendra el vector A
num_vec_a = int(input('Introduci el numero de iteraciones para el vector A'))
#Valida que no sean mayor a 15 elementos
while num_vec_a > 15 : 
    num_vec_a = int(input('ERROR - Introduci el numero de iteraciones'))
#Este for(ciclo de iteraciones) , se ocupa de preguntar al usuario que elementos introduce y de hacer append en el vector A(cargar el vector con los elementos)
for i in range(num_vec_a):
    num_elemento_a = int(input('Ingresa un numero'))
    vector_a.append(num_elemento_a)
    
num_vec_b = int(input('Introduci el numero de iteraciones para el vector B'))
while num_vec_b > 15 : 
    num_vec_b = int(input('ERROR - Introduci el numero de iteraciones'))
    
for i in range(num_vec_b):
    num_elemento_b = int(input('Ingresa un numero'))
    vector_b.append(num_elemento_b)
    
print(f'El vector A es el siguiente : {vector_a}')
print(f'El vector B es el siguiente : {vector_b}')
print(f'La suma de estos dos vectores es {vector_a + vector_b}')