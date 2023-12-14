#Dado un arreglo de n elementos, calcular e imprimir el menor de los múltiplos de 5 y el mayor de los múltiplos de 10. Determinar la posición de cada uno de ellos
vector_seba = []


long_vector = int(input('Introduce la logitud del vector'))
#Cargo el vector
for i in range(long_vector):
    elemento = int(input('Introduci un elemento del vector'))
    vector_seba.append(elemento)
#Guardo la posicion 0 del vector seba
min_mult_5 = vector_seba[0]
max_mult_10 = vector_seba[0]
pos_min = 0
pos_max = 0
#Trabajo con el vector
for i in range(len(vector_seba)):
    #Trabajo con el minimo multiplo de 5
    if vector_seba[i] < min_mult_5 and vector_seba[i] % 5 == 0: 
        min_mult_5 = vector_seba[i]
        pos_min = i
    #Trabajo con el meyor multiplo de 10
    if vector_seba[i] > max_mult_10 and vector_seba[i] % 10 == 0:
        max_mult_10 = vector_seba[i]
        pos_max = i
 
#Trabajo con la impresion de mis variable.       
if min_mult_5 % 5 == 0:
    print(f'El menor multiplo de 5 es {min_mult_5} y se encuentra en la posicion {pos_min} del vector')
else:
    print('No tiene multiplo de 5')
    
if max_mult_10 % 10 == 0:
    print(f'El mayor de los multiplos de 10 es {max_mult_10} y se encuentra en la posicion {pos_max} del vector')
else: 
    print('No tiene multiplo de 10')
    
    