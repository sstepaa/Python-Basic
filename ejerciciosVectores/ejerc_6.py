#Se pide cargar en memoria un arreglo de N posiciones.
#Se pide generar un programa que emita un ranking con los 10 números más grandes
#max_vector = vector_seba[0]
vector_seba = []
numero_vector = int(input('Ingrese el numero que quiera que tenga la logitud del vector'))

    
for i in range(numero_vector):
    elemento_vector = int(input('Ingrese un numero'))
    vector_seba.append(elemento_vector)
    
for i in range(len(vector_seba) - 1):
    for j in range(i + 1 , len(vector_seba)):
        if vector_seba[i] < vector_seba[j]:
            aux = vector_seba[i]
            vector_seba[i] = vector_seba[j]
            vector_seba[j] = aux


for i in range(10):
    print(vector_seba[i]) 

     
        
print(f'El vector completo es {vector_seba}')


