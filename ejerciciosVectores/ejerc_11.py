'''
Se dan 20 valores correspondientes a las estaturas de los alumnos de un curso A y 20 de un curso B.
Hallar:
a.Estatura máxima del curso A y del curso B y el lugar que ocupa alumno en la lista.
b.Comparar ambas estaturas e indicar cuál es la mayor imprimiendo un mensaje

'''

vector_A = []
vector_B = []
pos_max_A = 0
pos_max_B= 0
pos_max = 0
i = 0
while len(vector_A) < 3 :
    altura_alumno = float(input('Introducí la estatura de el alumno que asiste al curso A '))
    vector_A.append(altura_alumno)
    max_estatura_A = vector_A[0]
    if vector_A[i] > max_estatura_A :
        max_estatura_A = vector_A[i]
        pos_max_A = i
    i += 1

j = 0 
while len(vector_B) < 3 :
    altura_alumno = float(input('Introducí la estatura de el alumno que asiste al curso B '))
    vector_B.append(altura_alumno)
    max_estatura_B = vector_B[0]
    if vector_B[j] > max_estatura_B:
        max_estatura_B = vector_B[j]
    j += 1
    
if max_estatura_A > max_estatura_B :
    pos_max = max_estatura_A
else : 
    pos_max = max_estatura_B
    
print(f'El vector de estaturas de A es {vector_A} y el alumno con mayor estatura es el de la posicion : {pos_max_A} con {max_estatura_A} de alto')
print(f'El vector de estaturas de B es {vector_B} y el alumno con mayor estatura es el de la posicion : {pos_max_B} con {max_estatura_B} de alto')
print(f'El alumno mas alto de los dos curso es : {pos_max}')