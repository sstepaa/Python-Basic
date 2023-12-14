#Los datos a ingresar son :
#nro de factura 
#(Finaliza la carga cuando la factura es 0 , no puede ser negativo)
#Cantidad
#-Producto puede ser : 1-Memoria 2-CPU 3-Disco (El producto 1 vale : 100 , El producto 2 vale : 200, El producto 3 vale : 300)

#Se solicita obtener la sig informacion una vez finalizado la carga
#En cada venta se registra un solo producto 
#Total de unidades vendidas
#Factura de mayor cantidad
#Numero de factura con menos cantidad de productos solicitado
#Promedio de ventas en unidades

nro_facturas_vec = []
cantidades = []
acum_cantidades = 0

nro_factura = int(input('Ingrese su numero de factura'))
while nro_factura < 0 :
    nro_factura = int(input('Error - Ingrese su numero de factura'))
    
while nro_factura != 0 : 
    #Tengo un vector donde cargar los datos
    nro_facturas_vec.append(nro_factura)
    
    cantidad = int(input('Introduzca la cantidad'))
    while cantidad < 0:
         cantidad = int(input('Error - Introduzca la cantidad'))
    #Cargo el vector     
    cantidades.append(cantidad)
        
    nro_factura = int(input('Ingrese su numero de factura'))
    while nro_factura < 0 :
        nro_factura = int(input('Error - Ingrese su numero de factura'))

#Para cuando no haya error cuando ejecutas 0
if len(nro_facturas_vec) == 0:
    print('No hay datos para mostrar')
else :             
    for i in range(len(nro_facturas_vec)):
        print(f'Facturas {nro_facturas_vec[i]} cantidades {cantidades[i]}')
        
    for i in range(len(cantidades)):
        acum_cantidades += cantidades[i]
    print(f'Se vendieron un total de {acum_cantidades} unidades.')
    
    max_cant = cantidades[0]
    max_factura = nro_facturas_vec[0]
    
    for i in range(len(cantidades)):
        if max_cant < cantidades[i]:
            max_cant += cantidades[i]
            max_factura += nro_facturas_vec[i]
    print(f'La maxima factura es {max_factura} con {max_cant} unidades')
    
    min_cant = cantidades[0]
    min_factura = nro_facturas_vec[0]
    
    for i in range(len(cantidades)):
        if min_cant > cantidades[i]:
            min_cant += cantidades[i]
            min_factura += nro_facturas_vec[i]
    print(f'La minima factura es {min_factura} con {min_cant} unidades')