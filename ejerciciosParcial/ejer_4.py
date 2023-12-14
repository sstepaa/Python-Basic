# Para realizar una estadística la empresa "El estadista", le pide desarrollar un sistema que procese los datos solicitados en una encuesta.
# Para ello se carga la edad, cantidad de hijos y la provincia donde vive (se codifican de 1 a 10).
# La carga finaliza cuando se ingresa 0 en la edad o se hayan procesados mas de 1000 encuestas
# A partir de estos datos cargados se pide resolver las siguiente estadísticas:
# Mostrar todos los datos de los encuestados en forma de cuadro.
# Porcentaje de encuestados de cada provincia
# Indicar la edad y la provincia de la persona encuestada que tenga menos hijos.
# Promedio de edades de los encuestados de una provincia en particular (el dato de la provincia se debe pedir por teclado)
# Mostrar todos los datos de los encuestados ordenado por provincia en forma descendente

#El total es la suma de las provincias no el len del vector. hacer un sumador de las provincias ese seria el total para dividirlo por la parte y luego multiplicarlo por 100.


def cargaVec(vecEdad , vecHijos , vecProv):
    contEncuesta = 0
    numEdad = int(input('Ingresa su edad : '))
    #Bloque para verificar que el dato edad sea mayor a 0
    while numEdad < 0 : 
         numEdad = int(input('Error - Reingresa su edad : '))
    
    while numEdad != 0 or contEncuesta > 1000:
        vecEdad.append(numEdad)
        numHijos = int(input('Ingresa cuantos hijos tenes : '))
        #Validacion del dato hijos para que no sea un entero negativo
        while numHijos < 0 : 
            numHijos = int(input('Error - Reingresa cuantos hijos tenes : '))
        vecHijos.append(numHijos)
        
        numProv = int(input('Ingresa de que provincia sos (1 - 10) : '))
        while numProv <= 0 or numProv > 10:
             numProv = int(input('Error - Ingresa de que provincia sos (1 - 10) : '))
        vecProv.append(numProv)
        
        numEdad = int(input('Ingresa su edad : '))
def mostrar(vecEdad , vecHijos , vecProv):
    print('\n')
    for i in range(len(vecEdad)):
        print(f'Edad : {vecEdad[i]}\tHijos : {vecHijos[i]}\tProvincia : {vecProv[i]}')
def porcentaje(vec):
    vecContador = [0] * 10
    sumadorTotal = 0
    for i in range(len(vec)):
        if vec[i] == 1 : 
            vecContador[0] += 1
        elif vec[i] == 2:
            vecContador[1] += 1
        elif vec[i] == 3 :
            vecContador[2] += 1
        elif vec[i] == 4:
            vecContador[3] += 1
        elif vec[i] == 5:
            vecContador[4] += 1
        elif vec[i] == 6:
            vecContador[5] += 1
        elif vec[i] == 7:
            vecContador[6] += 1
        elif vec[i] == 8:
            vecContador[7] += 1
        elif vec[i] == 9:
            vecContador[8] += 1
        else : 
            vecContador[9] += 1
            
    for j in range(len(vecContador)):
        sumadorTotal += vecContador[j]
        
    return vecContador , sumadorTotal
def mostrarPorcProv(total , vec1 , vec2):
    print('\n')
    for i in range(len(vec1)):
        print(f'El porcentaje de la provincia {vec1[i]} es {(vec2[i] / total) * 100}% de encuestados')
def menosHijos(vecHijos) : 
    minHijos = vecHijos[0]
    pos = 0
    for i in range(len(vecHijos)):
        if vecHijos[i] < minHijos:
            minHijos = vecHijos[i]
            pos = i
    return minHijos , pos
def promedio(vec1, numProv):
    sumaEdades = 0
    contEdades = 0
    
    for i in range(len(vec1)):
        if vec1[i] == numProv:
            sumaEdades += vec1[i]
            contEdades += 1
            
    if contEdades == 0 :
        print('No hay datos')
        
    promedio = sumaEdades/contEdades
    return promedio
#Programa principal 
vectorEdad  = []
vectorHijos = [] 
vectorProv = []
cargaVec(vectorEdad , vectorHijos , vectorProv)
if len(vectorEdad) != 0 and len(vectorHijos) and len(vectorProv): 
    mostrar(vectorEdad ,  vectorHijos , vectorProv)
    
    
    # Porcentaje de encuestados de cada provincia
    vectorCantProv = porcentaje(vectorProv)
    vecContador , sumTotal = vectorCantProv 
    mostrarPorcProv(sumTotal , vectorProv , vecContador)
   
   
    # Indicar la edad y la provincia de la persona encuestada que tenga menos hijos.
    minCantHijos = menosHijos(vectorHijos)
    minHijos , posMinHijos = minCantHijos
    print(f'La persona que tiene menos hijos corresponde a la provincia {vectorProv[posMinHijos]} con la edad de {vectorEdad[posMinHijos]} siendo la cantidad de hijos total {minHijos}')
    
    
    # Promedio de edades de los encuestados de una provincia en particular (el dato de la provincia se debe pedir por teclado)
    numBusquedadProm = int(input('Ingrese que promedio de provincia buscar'))
    while numBusquedadProm <= 0 or numBusquedadProm > 10:
             numBusquedadProm = int(input('Error - Los numeros de provincias es de : 1 - 10  '))
    promedioProvincia = promedio(vectorEdad , numBusquedadProm)
    promedioP = promedioProvincia
    print(f'El promedio de edad de la provincia {numBusquedadProm} es {promedioP}')
    
else: 
    print('No hay datos para mostrar.')
