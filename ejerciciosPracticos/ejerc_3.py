#Ingresar números hasta que el último sea cero. Calcular la cantidad de positivos.
cont_positivos = 0
num = int(input('Ingrese un numero'))
while num != 0: 
    if num > 0 :
        cont_positivos += 1
    num = int(input('Ingrese un numero'))
    
print(f'Los numeros positivos que fueron ingresado fueron {cont_positivos}')