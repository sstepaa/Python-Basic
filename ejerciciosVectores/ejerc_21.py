'''Ingresar 10 números, cargar un arreglo donde los números pares estén en las posiciones pares y los números impares en las posiciones impares.
Calcular y mostrar:
a. El promedio de los números múltiplos de 5 que se encuentren las posiciones impares y la suma de las posiciones pares (en una función).
b. Cuántas veces aparece un número múltiplo de 4 en las posiciones pares.
c. Intercambiar cada número con su sucesor.
d. Contar en cuántas parejas de números el primero es menor que el segundo'''

vector_A = []

for i in range(5):
    num = int(input('Ingrese un numero'))
    if i % 2 == 0 : #Aca defino si la posicion es par
        if num % 2 == 0 : #Aca defino si el numero es par 
            vector_A.append(num)
        else:
            while num % 2 != 0:
                num = int(input('Ingrese un numero par , debido a que estamos en una posicion par')) 
            vector_A.append(num)
    
    if i % 2 != 0:
         if num % 2 != 0:
                vector_A.append(num)
         else:
             while num % 2 == 0:
                 num = int(input('Ingrese un numero impar , debido a que estamos en una posicion impar'))
             vector_A.append(num)
             
cont_mulp_5 = 0
acum_mulp_5 = 0
acum_pares = 0
cont_mult_4 = 0
for i in range(len(vector_A)):
    if vector_A[i] % 5 == 0 and i % 2 != 0: 
        cont_mulp_5 += 1
        acum_mulp_5 += vector_A[i]
        
    if vector_A[i] % 2 == 0 : 
        acum_pares += vector_A[i]
        
    if vector_A[i] % 4 == 0 and i % 2 == 0: 
        cont_mult_4 += 1
             
print(vector_A)
if cont_mulp_5 != 0  : 
    print(f'El promedio de los números pares a 5 en posicion impares es {acum_mulp_5 / cont_mulp_5}')
else:    
    print('No hay datos para calcular el promedio.')
    
if cont_mult_4 == 0 :
    print('No hay ningun multiplo de 4 en alguna posicion par.')
else:
    print(f'Hay {cont_mult_4} cantidad de numeros pares')
    
#c. Intercambiar cada número con su sucesor.
for k in range(0 , len(vector_A) -1, 2):
    var_aux = vector_A[k]
    vector_A[k] = vector_A[k + 1]
    vector_A[k + 1] = var_aux
    
print(f'El vector cuando intercambian las parejas queda {vector_A}')

#Contar en cuántas parejas de números el primero es menor que el segundo
cont_parejas_menores = 0
cont_parejas_mayores = 0
for j in range(0 , len(vector_A) -1):
    elemento1 = vector_A[j]
    elemento2 = vector_A[j + 1]
    
    if elemento1 < elemento2 : 
        cont_parejas_menores += 1
    else : 
        cont_parejas_mayores += 1
        
if cont_parejas_menores <= 0 : 
    print('No hay parejas con el elemento primero mayor al segundo')
    print(f'El numero de segunda posicion mayor al primero es {cont_parejas_mayores}')
else : 
    print(f'La cantidad de parejas con el primer elemento mayor es {cont_parejas_menores}')
    
