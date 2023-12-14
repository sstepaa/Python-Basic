'''
Calcular el sueldo de una persona, conociendo la cantidad de horas que trabaja en el mes y el valor de la hora.

'''

'''
Datos de entrada : Cantidad de horas que trabaja por mes y Valor de cada hora trabajada

Proceso : Multiplicar los valores ingresados

Informacion de salida : El resultado del producto representa el sueldo de la persona 

PRECONDICION = Cantidad de horas trabajadas , Valor por cada hora.
POSTCONDICION  = Sueldo de la persona.
'''

cantidad_horas = int(input('Ingresa la cantidad de horas trabajadas por mes'))
valor_horas = int(input('Ingresa el valor de la hora de trabajo'))

sueldo = cantidad_horas * valor_horas

print(f'El sueldo de la persona es de ${sueldo}')
