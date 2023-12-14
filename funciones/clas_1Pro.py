def obtenerEnteroPositivo():
    dato = int(input('Ingrese un numero positivo'))
    while dato < 0 : 
        print('Error , el numero debe ser positivo')
        dato = int(input('Ingrese un numero positivo'))
    return dato

def factorial(num):
    fact = 1
    for i in range(1 , num + 1):
        fact *= i
    return fact

def combinatorio(m, n):
    factM = factorial(m)
    factMN = factorial(m - n)
    factN = factorial(n)
    
    return factM / (factMN * factN)

def mostrar(resultado , m , n):
    print(f'El combinatorio entre {m} y {n} es {resultado}')
    
m = obtenerEnteroPositivo()
n = obtenerEnteroPositivo()
    
resultado = combinatorio(m ,n)
mostrar(resultado , m , n)