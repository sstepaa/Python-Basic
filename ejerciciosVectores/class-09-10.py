'''
La ferreterua 'El tornillo loco' , quiere llevar las ventas del mes para la cual necesita un programa que la asista.
Las ventas se cargan de la siguiente manera.
-Dia del mes (1-31)
-Articulo   -serrucho(500)
            -Motosierra(9500)
            -pinza de punta(450)        
-Cantidad solicitada

Se carga una sola herramienta por venta y se finaliza la lectura con el dia = 45
Se solicita:
-Dia de mayor venta (total de factura emitidas)
-Total recaudado
-Porcentaje de unidades por cada herramienta
-Porcentaje en pesos sobre el total vendido de c/herramienta
-Promedio de unidades vendidas 
-Ingresar un dia , y mostrar la cantidad de ventas realizadas (facturas emitidas)
vec_count = [] * 31
'''

dias_mes_vector = []
herramientas_vector = []
cantidades_vector = []
#Para las facturas
vector_cont = [0] * 31 #Contador de 31 elementos , Va de 0 30 el vector
max_contador = 0

PRECIO_SERRUCHO = 500
PRECIO_MOTOSIERRA = 9500
PRECIO_PINZA_PUNTA = 450 

dia_mes = int(input('Ingrese el dia del mes '))
while dia_mes != 45 : 
    while dia_mes < 1 or dia_mes >= 31 :
        dia_mes = int(input('Error ingrese devuelta el dia'))
    #Carga el vector dias   
    dias_mes_vector.append(dia_mes)
    
    herramienta = input('Serrucho , Motosierra , Pinza de punta')  
    while herramienta != 'Serrucho' and herramienta != 'Motosierra' and herramienta != 'Pinza de punta':
             herramienta = int(input('ERROR -Serrucho , Motosierra , Pinza de punta'))  
    herramientas_vector.append(herramienta)
    
    cantidad = int(input('Ingrese la cantidad que compro del producto'))
    while cantidad < 0 or cantidad == 0 : 
        cantidad = int(input('ERROR - Ingrese la cantidad que compro del producto'))
    cantidades_vector.append(cantidad)
    
    #Manejo de dato de corte dia
    dia_mes = int(input('Ingrese el dia '))
    
#Cargo el contador con los dias que se facturaron cada articulo
for dia in dias_mes_vector:
    vector_cont[dia - 1] += 1 
#Buscar el maximo en el vector contador
for i in range(len(vector_cont)) : 
    if max_contador < vector_cont[i]:
        max_contador = vector_cont[i]
    
print(dias_mes_vector)
print(herramientas_vector)
print(cantidades_vector)
print(vector_cont)
print(f'El dia que se facturaron mas fue : {max_contador}')

    


