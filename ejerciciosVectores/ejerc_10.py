#Generar un arreglo P con los 15 primeros números primos. Mostrarlo
vector_p = []
vector_noP = []

i = 0
while len(vector_p) < 15:
    i += 1#Indice del vector
    num_elemento = int(input('Ingresa un numero'))
    #Validar los numeros negativos
    while num_elemento <= 1:
        num_elemento = int(input('Error - Ingresa un numero'))
    
    if num_elemento > 1 :
        cont_no_P  = 0 
        for j in range(2 , num_elemento):
            resto = num_elemento % j
            if resto == 0 :
                cont_no_P += 1
        
        if cont_no_P == 0:
            print(f'El numero {num_elemento} es primo y se agrega a el vector de numeros primos')
            vector_p.append(num_elemento) 
        else : 
            print(f'El numero {num_elemento} no es primo y se agrega al vector de numeros no primos')
            vector_noP.append(num_elemento)

print(f'El vector con numeros primos es : {vector_p} ')
print(f'El vector con numeros NO primos es : {vector_noP} ')