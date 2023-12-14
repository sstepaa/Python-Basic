# Se ingresan la cantidad de kilos vendidos de chocolate amargo y semiamargo (dos vectores) a lo largo de el mes de junio (30 días). 
# El valor del kilo de chocolate amargo es $3000 y el valor del kilo del chocolate semiamargo es de $3200.
# Calcular y mostrar:
# El día del mes donde se vendió menos kilos de chocolate amargo y el día del mes donde se vendió la menor cantidad de chocolate semiamargo.
# Tipo de chocolate que más recaudó teniendo en cuenta el promedio de sus ventas en pesos.
# Crear un nuevo arreglo con la suma de los kilos vendidos por día.
VALUEAMARGO = 3000
VALUESEMIAMARGO = 3200

def cargaChoco(vecAmargo , vecSemi ):
    for i in range(4) : 
        #Carga del vector Chocolate Amargo
        cantAmargo = int(input('Ingrese la cantidad que ha comprado de chocolate amargo : '))
        while cantAmargo < 0 :
            cantAmargo = int(input('ERROR - Ingrese la cantidad que ha comprado de chocolate amargo : '))
        vecAmargo.append(cantAmargo)
        
        #Carga del vector Chocolate Semiamargo
        cantSemiAmargo = int(input('Ingrese la cantidad de que ha comprado de chocolate semi amargo : '))
        while cantSemiAmargo < 0 : 
            cantSemiAmargo = int(input('ERROR - Ingrese la cantidad de que ha comprado de chocolate semi amargo : '))
        vecSemi.append(cantSemiAmargo)
        
def minChoco(vec): 
    minChoco = vec[0]
    diaMinimo = 0
    for i in range(len(vec)):
        if minChoco > vec[i]:
            minChoco = vec[i]
            diaMinimo = i
    return diaMinimo, minChoco

def recaudacion(vec , value):
    sumCant = 0
    for i in range(len(vec)):
        sumCant += vec[i]
    
    totalvalue = sumCant * value 
    promTotalValue = (totalvalue) / len(vec)
    return totalvalue , promTotalValue
        
def newVector(vecAmargo , vecSemi): 
    if len(vecSemi) == len(vecAmargo): #Primero corroborar si los dos vectores tienen la misma longitud , si no la tienen no se va a poder realizar la suma.
        newVector = []
    
    for i in range(len(vecAmargo)):
        suma = vecAmargo[i] + vecSemi[i]
        newVector.append(suma)
        
    return newVector     
        
# programa principal
vecAmargo = []
vecSemiAmargo = []
cargaChoco(vecAmargo , vecSemiAmargo)
if len(vecAmargo) == 0 and len(vecSemiAmargo) == 0:
    print('No hay datos para mostrar')
else:
    print(f'Vector chocolate amargo : {vecAmargo}')
    print(f'Vector chocola semi amargo : {vecSemiAmargo}')
    
    resultadoCMinimo = minChoco(vecAmargo)
    resultadoCSemiAmargoMinimo = minChoco(vecSemiAmargo)
    diaMinimoAmargo , cantMinimoAmargo = resultadoCMinimo
    diaMinimoSemi , cantMinimoSemi = resultadoCSemiAmargoMinimo    
    
    print(f'El día del mes donde se vendió menos kilos de chocolate amargo fue {diaMinimoAmargo} , se compro la cantidad de {cantMinimoAmargo} KG')
    print(f'La cantidad minima de chocolate semi-amargo es {cantMinimoSemi} KG y fue hecha en el dia {diaMinimoSemi} ')
    
    #Recaudacion de chocolate amargo
    recaudacionAmargo = recaudacion(vecAmargo , VALUEAMARGO)
    valorTotalAmargo , promTotalAmargo = recaudacionAmargo
    #Recaudacion de chocolate amargo
    
    #Recadacion de chocolate semi-amargo
    recaudacionSemiAmargo = recaudacion(vecSemiAmargo , VALUESEMIAMARGO)
    valorTotalSemi , promTotalSemi = recaudacionSemiAmargo
    #Recadacion de chocolate semi-amargo
    
    print(f'La recaudacion total de los chocolates amargos es de ${valorTotalAmargo} y su promedio de venta es de ${promTotalAmargo}')
    print(f'La recaudacion total de los chocolates semi-amargo es de ${valorTotalSemi} y su promedio de venta es de ${promTotalSemi}')
    if promTotalSemi > promTotalAmargo : 
        print(f'El tipo de chocolate que recaudo mas fue el chocolate semi-Amargo')
    else : 
        print(f'El tipo de chocolate que recaudo mas fue el chocolate Amargo')
    
    vectorSuma = newVector(vecAmargo, vecSemiAmargo)
    vecCantTotal = vectorSuma
    print(f'El vector con la suma de las cantidades es {vecCantTotal}')