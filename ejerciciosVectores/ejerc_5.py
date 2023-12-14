#Dado un arreglo, imprimir el lugar que ocupa el mínimo. Tener en cuenta que este valor puedeestar repetido, en ese caso imprimir todos los lugares donde aparece este valor.
vector_seba = [3 ,4 ,3 ,6, 7, 9]
vector_minimo_rep = []
min_value = vector_seba[0]

for i in range(len(vector_seba)):
    if min_value > vector_seba[i]:
        min_value = vector_seba[i]
        vector_minimo_rep = [min_value]
    elif min_value == vector_seba[i]:
        vector_minimo_rep.append(min_value)
        
        
print(f'El valor minimo de este vector es {min_value}')
print(f'El indice que ocupa los valores repetivos son {vector_minimo_rep}')