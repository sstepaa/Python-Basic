'''
Ingresar 12 números, cargar un arreglo, calcular y mostrar:
a. El máximo de los números múltiplos de 2 y su posición.
b. El mínimo de los números impares y su posición.
c. Intercambiar el primer número con el último y así sucesivamente.
d. Reemplazar con 0 a las parejas de números cuyo promedio supera a 5.
'''

vector_A = []
pos_max_mult = 0
pos_min_mulp = 0 

i = 0
while len(vector_A) < 8 : 
    num = int(input('Ingrese un numero'))
    vector_A.append(num)
    
max_multp = vector_A[0]
min_multp = vector_A[0]

for i in range(len(vector_A)):
    if vector_A[i] > max_multp and num % 2 == 0: 
        max_multp = vector_A[i]
        pos_max_mult = i
    if   vector_A[i] < min_multp and num % 2 == 1:
        min_multp = vector_A[i]
        pos_min_mulp = i
    
    

print(f'El vector es : {vector_A}')
print(f'El valor par maximo en el vector es {max_multp} y corresponde a la posición {pos_max_mult}')
print(f'El valor minimo del vector es {min_multp} y corresponde a la posición {pos_min_mulp}')


for j in range(len(vector_A) // 2):
    var_aux = vector_A[j]
    vector_A[j] = len(vector_A) -1 -j
    vector_A[len(vector_A)-1 -j] = var_aux
print(f'Vector que intercambia sus posiciones es {vector_A}')

for k in range(0 , len(vector_A) , 2):
     elemento1 = vector_A[k]
     elemento2 = vector_A[k + 1]
     
     suma = elemento1 + elemento2
     
     pareja = vector_A[k:k+2] #Selecciono las parejas de a dos en el vector
     print(f'pareja : {pareja}')
     
     promedio = suma / 2
     print(f'La suma de los pares son {suma} y su promedio es {promedio}')
     if promedio > 5 :
            vector_A[k] = 0
            vector_A[k + 1] = 0
         

print(k)
         
         
print(vector_A)