#Ingresar un arreglo de 10 componentes:
#a.Imprimir la cuarta componente.
#b.Imprimir los componentes en orden invertida.
#c.Imprimir el producto entre la primera y la última componente.
#d.Imprimir las componentes de índice impar.
#e.Imprimir la suma de las componentes de índice par.
#f.Imprimir la multiplicación de las componentes de índice impar.
#g.Imprimir el arreglo que resulta de intercambiar la primera con el última componente
vectorS = [2 ,3 , 5 , 3 , 2 , 4 , 5 , 7 , 8 , 9 ]

#a 
print(vectorS[3])
#b
for i in range(len(vectorS)//2):
    vec_aux = vectorS[i]
    vectorS[i] = len(vectorS) - 1 - i
    vectorS[len(vectorS) - 1 - i] = vec_aux
print(f'El vector invertido es {vectorS}')
#c 
prod = vectorS[0] * vectorS[-1]
print(f'La multiplicacion entre el primer item y el ultimo')
#d 
for i in range(len(vectorS)):
    if vectorS[i] % 2 == 0:
        print(vectorS[i])
#e
acum_par = 0
for i in range(len(vectorS)):
    if vectorS[i] % 2 == 0:
        acum_par += vectorS[i]
        
print(f'La suma de los numeros pares es {acum_par}')

#f.Imprimir la multiplicación de las componentes de índice impar.
num_impar = 0
acum_impar = 0
for i in range(len(vectorS)):
    if vectorS[i] % 2 == 1:
        acum_impar += 1
        num_impar += vectorS[i]
             
print(f'La multilicacion de los numeros impares son {acum_impar * num_impar}')

#g.Imprimir el arreglo que resulta de intercambiar la primera con la última componente
var_aux = vectorS[0]
vectorS[0] = vectorS[-1]
vectorS[-1] = var_aux 
print(f'El vector con el intercambio de posicion es {vectorS}' )
