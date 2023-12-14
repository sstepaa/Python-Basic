'''
Construir una función que permita devolver el valor absoluto de un número ingresado por teclado
'''

def pedir():
    num = int(input('Ingrese un numero'))
    return num

def valorAbsoluto(numero):
    if numero < 0 : 
        numero = - numero
    return numero

num = pedir()
print(valorAbsoluto(num))
