'''
Se han analizado N < 12 temperaturas correspondientes a N variaciones de volumen cuando la presión es constante.
Datos:
N:cantidad total de temperaturas y volúmenes
T:temperatura
V:volumen
Hallar y mostrar:
a.Temperatura máxima y mínima registrada.
b.Volúmenes correspondientes a cada una de ellas.
c.Ordenar el arreglo de las temperaturas de mayor a menor e imprimirlas.
'''

vector_T = []
vector_V = []

N = int(input('Ingrese la cantidad total de temperaturas'))
while N > 12 :
    N = int(input('Error - Ingrese la cantidad una cantidad menor a 12. '))

for i in range(N):
    #Pido los datos al usurario para cargar los dos vectores
    T = float(input(f'Ingrese la temperatura {i + 1} : '))
    V = float(input(f'Ingrese el volumen {i + 1} : '))
    
    vector_T.append(T)#Cargo el vector con el dato en T
    vector_V.append(V)#Cargo el vector con el dato en V

max_T = vector_T[0]
min_T = vector_T[0]

max_V = vector_V[0]
min_V = vector_V[0]

#Vamos a buscar el maximo y minimo.
for i in range(len(vector_T)):
    if vector_T[i] > max_T:
        max_T = vector_T[i]
        max_V = vector_V[i]
        
    if vector_T[i] < min_T:
        min_T = vector_T[i]   
        min_V = vector_V[i]
        
        
#PUNTO A RESUELTO   
print(f'La mayor temperatura registrada fue {max_T} , con un volumen de {max_V}.')
print(f'La menor temperatura registrada fue {min_T} , con un volumen de {min_V}.') 
#Ordenar el vector de forma asendente (Mayor a menor)
vector_T.sort(reverse=True)
print(f'Las temperaturas de ordenadas son {vector_T}')


    