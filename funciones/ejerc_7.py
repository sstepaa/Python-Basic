'''
Se ingresan la cantidad de kilos vendidos de chocolate amargo y semiamargo (dos vectores) a lo largo de el mes de junio (30 días).
El valor del kilo de chocolate amargo es $3000 y el valor del kilo del chocolate semiamargo es de $3200.

Calcular y mostrar

El día del mes donde se vendió menos kilos de chocolate amargo y el día del mes donde se vendió la menor cantidad de chocolate semiamargo.
Tipo de chocolate que más recaudó teniendo en cuenta el promedio de sus ventas en pesos.
Crear un nuevo arreglo con la suma de los kilos vendidos por día
'''

CHOCO_AMARGO = 3000
CHOCO_SEMIAMARGO = 3200

def carga(vec1 , vec2):
    while len(vec1) < 3 :
        choco_am = int(input('Ingrese la cantidad de chocolate amargo vendida'))
        vec1.append(choco_am)
        
    while len(vec2) < 3:
        choco_semi_am = int(input('Ingrese la cantidad de chocolate semi amargo vendida'))
        vec2.append(choco_semi_am)
cant_ch_amargo = []
cant_ch_semiamargo = []
carga(cant_ch_amargo , cant_ch_semiamargo)

print(cant_ch_amargo)
print(cant_ch_semiamargo)