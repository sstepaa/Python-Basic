'''
Ingresar números hasta cargar un arreglo de 10 elementos de la siguiente manera:
5 positivos y 5 negativos en ese orden.
Calcular y mostrar:
a.El promedio de los números negativos.
b.Ordenar el arreglo de menor a mayor.
c.Generar otro arreglo con los múltiplos de 4. Si no los hubiese mostrar cartel aclaratorio.
d.Mostrar cuántos pares y cuántos múltiplos de 3 hay en este último arreglo.
'''
vector_A = []
vector_A_M = []
i = 0
#Contadores
positivos = 0 
negativos = 0
cont_par = 0

#acumuladores
sum_negativo = 0

while len(vector_A) < 4 : 
    num = int(input('Ingrese un numero'))
    
    if num > 0 and positivos < 2 :
        vector_A.append(num)
        positivos += 1
        
        if num % 2 == 0 and num % 3 == 0:
            cont_par += 1
    
    elif num < 0 and negativos < 2 :
        negativos += 1
        vector_A.append(num)
        sum_negativo += num
        
        if num % 2 == 0 and num % 3 == 0:
            cont_par += 1
        
    else : 
            print("El número no cumple con los requisitos. Ingrese otro número.")
    
    i += 1
    
for i in range(len(vector_A)):
    if vector_A[i] % 4 == 0:
        vector_A_M.append(vector_A[i])
    
    
print(f'vector A : {vector_A}' )

if sum_negativo == 0 :
    print('No hay suficientes datos')
else:
    print(f'El promedio de los negativos es {sum_negativo/negativos}')
    
if len(vector_A_M) == 0 : 
    print('No hay datos en el vector')
else : 
    print(f'En el vector A se encontro estos numeros multiplos de 4 {vector_A_M}')

vector_A.sort(reverse=True)
print(f'El vector ordenado de mayor a menor {vector_A} ')

if cont_par == 0 : 
    print('No hay datos para mostrar')
else:
    print(f'La cantidad de numeros par y multiplos de tres son {cont_par}')