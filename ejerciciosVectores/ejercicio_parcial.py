#Los datos a ingresar son : 
#-NroFactura
#Finalizar la carga cuando la factura sea 0 , no puede ser negativo
#Nombre del cliente 
#-Producto puede ser : 1-Memoria 2-CPU 3-Disco
#El producto 1 vale :100 , el 2 vale : 200 , el 3 vale : 300
#Cantidad

#Se solicita obtener la siguiente informacion una vez finalizado la carga 
#En cada venta se registra un solo producto
#Total de la factura 
#Factura de mayor importe
#Factura con menor cantidad de producto solicitados
PRECIOUNO = 100
PRECIODOS = 200
PRECIOTRES = 300
contUno = 0 
contDos= 0 
contTres = 0
totalFacturado = 0
cantidadUno = cantidadDos = cantidadTres = 0

nroFactura = int(input('Ingrese numero de factura'))

#Validacion de el nro de factura para que todo lo que sea negativo lo filtro
while nroFactura < 0:
    nroFactura = int(input('Error-Ingrese numero de factura'))
#Validacion de el nro de factura para que todo lo que sea negativo lo filtro
while nroFactura != 0 : 
    cliente = input('Ingrese el nombre del cliente')
    producto = int(input('Ingrese el codigo del producto  1-Memoria 2-CPU 3-Disco'))
    
    while producto < 1 or producto > 3:
        producto = int(input('Error - Ingrese el codigo del producto  1-Memoria 2-CPU 3-Disco'))
        cantidad = int(input('Ingrese la cantidad de productos'))
        while cantidad < 0: 
            cantidad = int(input('Error -Ingrese la cantidad de productos'))
    #Total facturado
        if producto == 1:
            precioParcial = PRECIOUNO
            contUno += 1
            cantidadUno = cantidad
        elif producto == 2 :
            precioParcial = PRECIODOS
            contDos += 1
            cantidadDos = cantidad
        else : 
            precioParcial = PRECIOTRES
            contTres += 1
            cantidadTres = cantidad
        #Maximo  
        totalFactura = precioParcial * cantidad 
        if totalFacturado == 0 :
            maxFacturas = nroFactura
            maxImporte = totalFactura
            minFactura = nroFactura
            minCantidad = cantidad
        else : 
            #Maximo
            if maxImporte < totalFactura:
                maxFacturas = nroFactura
                maxImporte = totalFactura
            #Maximo
            #Minimo
            if minCantidad > cantidad:
                minFactura = nroFactura
                minCantidad = cantidad
            #Minimo    
        totalFacturado += precioParcial * cantidad 
    #Total facturado 
    
       
    nroFactura = int(input('Ingrese numero de factura'))
    #Validacion de el nro de factura para que todo lo que sea negativo lo filtro
    while nroFactura < 0:
        nroFactura = int(input('Error-Ingrese numero de factura'))
    #Validacion de el nro de factura para que todo lo que sea negativo lo filtro
    
if totalFacturado == 0 : 
    print('No se registraron ventas')
else: 
    print(f'El total facturado es de {totalFacturado}')
    print(f'La factura con mayor importe fue {maxFacturas} con el importe {maxImporte}')
    print(f'La factura con menor cantidad de productos fue {minFactura} con la cantidad de {minCantidad}')
    mayorCantidad = contUno
    mayorVendido = 'Memoria' 
    if mayorCantidad < contDos:
        mayorCantidad = contDos
        mayorVendido = 'CPU'
    if mayorCantidad < contTres :
        mayorCantidad = contTres
        mayorVendido = 'Disco'
        
    print(f'El mas vendido fue {mayorVendido} con la cantidad de {mayorCantidad} de veces')
    if contUno != 0:
        print(f'El promedio de memorias es {cantidadUno / contUno}')
    else:
        print('No se vendieron memorias')
        
    if contDos != 0 : 
        print(f'El promedio de memorias es {cantidadDos / contDos}')
    else:
        print('No se vendieron CPU')
        
    if contTres != 0:
        print(f'El promedio de memorias es {cantidadTres / contTres}')
    else:
        print('No se vendieron Disco')