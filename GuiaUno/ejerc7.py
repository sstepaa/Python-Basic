# Leer 15 números y generar un arreglo con los primeros 8 números mayores que 20.
# Si no hay 8 números que cumplan la condición, repetir el último hasta completar el arreglo.
# Si ningún número era mayor que 20, mostrar mensaje y salir.
# a) Calcular el promedio de los números que no entraron en el arreglo.
# b) Buscar el máximo elemento y mostrar el elemento que esté en la posición anterior. El máximo puede estar repetido.

def carga(vec):
    vecNo = []
    for i in range(5):
        num = int(input('Ingresa un numero'))
        if num >= 20 : 
            vec.append(num)
            
        