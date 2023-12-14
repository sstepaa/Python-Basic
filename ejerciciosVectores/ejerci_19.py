'''
Cargar un arreglo A de números enteros con los números que sean pares entre los primeros 15 ingresados.
Mostrarlo.
Generar un segundo arreglo B con los elementos de A que sean menores que el promedio de A. 
Mostrarlo
'''

vector_A = []
vector_B = []

cont_par = 0
acum_par = 0

while len(vector_A) < 6:
    num = int(input('Enter your number'))
    
    if num % 2 == 0 : 
        vector_A.append(num)
        cont_par += 1
        acum_par += num
    else : 
        print('Error Its number is not even ')
promedio_par = acum_par/cont_par

for i in range(len(vector_A)):
    if vector_A[i] < promedio_par:
        vector_B.append(vector_A[i])

print(f'El arreglo de numeros pares es : {vector_A}')
print(f'The average of the even numbers is : {promedio_par}')
if len(vector_B) == 0 :
    print('No hay datos en el vector')
else:
    print(f'El vector con los números menores al promedio de A es : {vector_B}')