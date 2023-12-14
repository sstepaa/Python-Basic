# Alicia y Hugo, poseen una empresa de venta de alimentos para mascotas y le solicitan a ud. la realización de un programa informático.
# Puntualmente el sistema que le solicitan es de registro de ventas. Este registro se realiza al finalizar el día.
# 1- Se cargan facturas HASTA QUE el número de factura sea 0. (EL NUMERO DE FACTURA NO PUEDE SER NEGATIVO). Y una vez cargado el numero de la factura se carga el importe. (dos vectores)
# 2- Se muestran los números de facturas con sus importes
# 3- Se calcula el importe máximo facturado y a que factura pertenece.
# 4- Se reemplaza el valor máximo facturado por , el valor consecutivo del máximo.
# 5- Calcular el promedio de los importes, e insertar después de cada valor superior al promedio, un -2 en ambos vectores
# 6- Se eliminan los números de facturas impares y los valores asociados a ellas

def carga(vecFacturas , vecImporte): 
    numFactura = int(input('Ingrese el número de factura: '))
    #Validación del dato factura , para que no sea un entero negativo.
    while numFactura < 0: 
        numFactura = int(input('Error - Reingrese el número de factura: '))
    #Validación del dato factura , Mientras que el dato ingresado no sea 0 , el bucle va a seguir.
    while numFactura != 0 :
        vecFacturas.append(numFactura)
        numImporte = int(input('Ingrese el importe de la factura : '))
        #Validacion del dato importe para que no sea un entero negativo.
        while numImporte <= 0 :
            numImporte = int(input('Error - Reingrese el importe de la factura : '))
        vecImporte.append(numImporte)
        
        numFactura = int(input('Ingrese el número de factura : '))
        
def mostrar(vec1 , vec2):
    print('\n')
    for i in range(len(vec1)):
        print(f'Facturas : {vec1[i]}\t Importes : {vec2[i]}')
        
def maxFacturado(vec1):
    maxCantImporte = vec1[0]
    pos = 0
    for i in range(len(vec1)):
        if vec1[i] > maxCantImporte:
            maxCantImporte = vec1[i]
            pos = i
    return  pos , maxCantImporte

def remplazoValorMax(posMax , vec):
    if posMax != len(vec) - 1:
        vec[posMax] = vec[posMax + 1]
    else : 
        print('El valor maximo está en la última posición.')
    return vec

def promedio(vec1 , vec2):
    sumaImportes = 0
    j = 0
    for i in range(len(vec1)):
        sumaImportes += vec1[i]
    promedioImporte = sumaImportes / len(vec1)
    
    while j < len(vec1):
        if vec1[j] > promedioImporte:
            vec1.insert(j + 1  ,-2)
            vec2.insert(j + 1 , -2)
            j += 1
        j += 1
    return promedioImporte , vec1 , vec2

def deleteFac(vec1 , vec2):
    i = 0 
    while i < len(vec1) : 
        if vec1[i] % 2 == 1 :
            vec1.pop(i)
            vec2.pop(i)
        else : 
            i += 1
#Programa principal
vectorFactura = []
vectorImporte = []
carga(vectorFactura , vectorImporte)
if len(vectorFactura) == 0 and len(vectorImporte) == 0:
    print('No hay datos para mostrar')
else:
    mostrar(vectorFactura , vectorImporte)

    maximo = maxFacturado(vectorImporte)
    posicionMax , importeMax  = maximo
    print(f'El maximo facturado es de ${importeMax} y corresponde a la factura {vectorFactura[posicionMax]}')
    vecMaxReemplazo = remplazoValorMax(posicionMax , vectorImporte)
    print(f'El vector modificado es {vecMaxReemplazo} ')

    funcionImporteProm = promedio(vectorImporte , vectorFactura)
    promImport , vectorFacMod , vectorImportMod = funcionImporteProm
    mostrar(vectorFactura , vectorImporte)
    print(f'El promedio de los importes es ${promImport}')

    deleteFac(vectorFactura , vectorImporte)
    mostrar(vectorFactura , vectorImporte)

