def factorial(num):
    fact = 1
    for i in range(1 , num + 1):
        fact *= i
    return fact

n = int(input('Ingrese un numero positivo'))
while n < 0 : 
    print('Error , el numero debe ser positivo')
    n = int(input('Ingrese un numero positivo'))
m = int(input('Ingrese un numero positivo'))
while m < 0 : 
    print('Error , el numero debe ser positivo')
    m = int(input('Ingrese un numero positivo'))

factM = factorial(m)
factMN = factorial(m - n)
factN = factorial(n)

resultado = factM / (factMN * factN)

print(resultado)



