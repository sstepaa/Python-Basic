'''
Para realizar una estadística la empresa "El estadista", le pide desarrollar un sistema que procese los datos solicitados en una encuesta.
Para ello se carga la edad, cantidad de hijos y la provincia donde vive (se codifican de 1 a 10).
La carga finaliza cuando se ingresa 0 en la edad o se hayan procesados mas de 1000 encuestas

A partir de estos datos cargados se pide resolver las siguiente estadísticas:

Mostrar todos los datos de los encuestados en forma de cuadro.
Porcentaje de encuestados de cada provincia
Indicar la edad y la provincia de la persona encuestada que tenga menos hijos.
Promedio de edades de los encuestados de una provincia en particular (el dato de la provincia se debe pedir por teclado)
Mostrar todos los datos de los encuestados ordenado por provincia en forma descendente.

'''
edades = []
cant_hijos = []
provincias = []

cont_encuesta = 0
#promedio de las provincias
acum_prov = 0
#promedio de las provincias
i = 0
#Pedimos el dato que va a manejar el corte del programa
element_edad = int(input('Ingrese la edad'))
while element_edad < 0 : 
    element_edad = int(input('Error - Reingrese la edad'))

while element_edad != 0: 
    edades.append(element_edad)

    hijos = int(input('Ingrese la cantidad de hijos que tenga'))
    while hijos < 0 : 
        hijos = int(input('Error Ingrese la cantidad de hijos que tenga'))
    cant_hijos.append(hijos)
    
    element_provincia = int(input('Indique de que provincia es (1 - 10) '))
    while element_provincia < 1 or element_provincia > 10 : 
        element_provincia = int(input('Error -Indique de que provincia es (1 - 10) '))
    provincias.append(element_provincia)
    
    #Volvemos a pedir ese mismo dato , para validar la entrada al ciclo
    element_edad = int(input('Ingrese la edad'))
    while element_edad < 0 : 
        element_edad = int(input('Error - Reingrese la edad'))
    i += 1
    

#Mostrar todos los datos de los encuestados en forma de cuadro.
for i in range(len(edades)):
    print(f'{edades[i]}\t{cant_hijos[i]}\t{provincias[i]}')
    
#Porcentaje de encuestados de cada provincia(1 - 10)
cont_prov = [0] * 10
total_provincias = len(provincias)
for provincia in provincias:
    cont_prov[provincia - 1]+= 1
    
#Para sacar el porcentaje 
for i in range(len(cont_prov)):
    cantidad = cont_prov[i]
    porcentaje = (cantidad / total_provincias) * 100
    print(f'Provincia {i + 1} : {porcentaje:.2f}%  ')
    
print(f'El vector de total de encuestado por provincia es de {cont_prov}')
    

#Indicar la edad y la provincia de la persona encuestada que tenga menos hijos.
min_cant_hijos = cant_hijos[0]
min_provincias = provincias[0]
min_edad = edades[0]
for i in range(len(cant_hijos)):
    if min_cant_hijos > cant_hijos[i]:
        min_cant_hijos = cant_hijos[i]
        min_provincias = provincias[i]
        min_edad = edades[i]

print(f'La edad de la persona con menos hijos es {min_edad} , pertenece a la provincia {min_provincias} y tiene {min_cant_hijos} de hijos')

'''#Promedio de edades de los encuestados de una provincia en particular (el dato de la provincia se debe pedir por teclado)
Mostrar todos los datos de los encuestados ordenado por provincia en forma descendente.'''
for i in range(len(provincias)):
    