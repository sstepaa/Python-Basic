'''
Se quiere controlar las bicicletas vendidas en un mes
los precios son paseo P a $60.000 y todo terreno T a $75.000 
La carga termina cuando el número de factura es -1 o se llega a las 1000 ventas
* Se pide la cantidad vendida
* Calcular el promedio de bicicletas de paseo vendidas
* El total vendido en monto.
* El porcentaje vendido de cada tipo de bicileta en pesos
* Cual fue el modelo mas vendido (unidades)
* El nombre de la persona que mas compro y el tipo
* La factura de la menor venta individual y el monto de la misma

Se considera que se vende un sólo tipo por factura
X cada venta se carga:
    Nº factura
    Tipo de bicicleta
    Nombre del comprador
    Cantidad
'''

BICIPASEO = 60
BICITODOTERRENO = 75
tope = 3
#Contadores
contTotal = 0

#Comienza la validacion de los datos de entrada
nroFactura = int(input("introduzca su numero de factura"))
while nroFactura < -1 : 
    nroFactura = int(input("Error- introduzca su numero de factura"))
    
    
while nroFactura != -1 and contTotal < tope:
    #se llega a las 1000 ventas , cuenta si las ventas llegan a 1000 
    cliente = input('Intruduzca el nombre del cliente')
    bici_opcion = int(input('Bici paseo (1) , Bici todo terreno (2)'))
    while bici_opcion < 1 or bici_opcion > 2 : 
        bici_opcion = int(input('Error Bici paseo (1) , Bici todo terreno (2)'))
    contTotal += 1
    
    #Bloque validacion de nroFactura
    nroFactura = int(input("introduzca su numero de factura"))
    while nroFactura < -1 : 
        nroFactura = int(input("Error- introduzca su numero de factura"))
    #Bloque validacion de nroFactura


print(contTotal)