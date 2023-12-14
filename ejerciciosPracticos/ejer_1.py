#Ingresar números hasta un múltiplo de 3. Mostrar el último número ingresado

num = int(input('Ingrese un numero'))

while num % 3 == 1 and num != 0:
        
    num = int(input('Ingrese un numero'))
    
print(f'El ultimo numero {num}')