#Cargar dos arreglos de enteros de N y M posiciones. Se pide generar un programa que produzca la intersección entre los dos arreglos.

vector_A = []
vector_B = []
vector_Inter = []
#Carga de vector A
log_vector_A = int(input('Introduzca la logitud del vector A'))
for i in range(log_vector_A):
    elemento_A = int(input('Ingrese un elemento'))
    vector_A.append(elemento_A)
    
log_vector_B = int(input('Introduzca la longitud del vector B'))
for u in range(log_vector_B):
    elemento_B = int(input('Ingrese un elemento'))
    vector_B.append(elemento_B)
    
    
for i in range(len(vector_A)):
    for j in range(len(vector_B)):
        if vector_A[i] == vector_B[j]:
            vector_Inter.append(vector_A[i])
    
print(f'Vector A : {vector_A}')
print(f'Vector B : {vector_B}')
print(vector_Inter)


    