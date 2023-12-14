#Calcular el promedio semanal de gastos en un mes, ingresando como datos: Semana número Gasto semanalEl proceso termina cuando “semana número” es igual a 5.
gasto_acum = 0
cont_semana = 0
num_semana = int(input('Ingrese el numero de semana'))
while num_semana > 5 or num_semana == 0:
    num_semana = int(input('Error - Ingrese el numero de semana'))
    
while num_semana != 5:
    gasto_semanal = int(input('Ingrese su gasto semanal'))
    gasto_acum += gasto_semanal
    cont_semana += 1
    
    num_semana = int(input('Ingrese el numero de semana'))
    while num_semana > 5:
        num_semana = int(input('Error-Ingrese el numero de semana'))
if cont_semana == 0 :
    print('No se ingreso ninguna semana')
else:
    print(f'El promedio de gasto semanal por mes es de {gasto_acum / cont_semana} , con un gasto total de ${gasto_acum}')