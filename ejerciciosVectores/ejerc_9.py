#Revertir un arreglo de 16 componentes sobre él mismo, es decir, poner el primer elemento en el último lugar y el último en el primer lugar, el segundo en el penúltimo y este en el segundo, etc.Decir si el arreglo es capicúa.

vector_stepa = [23,4,5,78,6,3,2,44,12,14,13,15,16,17,66,29]

for i in range(len(vector_stepa) // 2):
    var_aux = vector_stepa[i]
    vector_stepa[i] = len(vector_stepa) -1 -i
    vector_stepa[len(vector_stepa) -1 -i] = var_aux
    
print(vector_stepa)