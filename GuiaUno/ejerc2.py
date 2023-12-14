'''
Convertir longitudes de millas a Km. y de pulgadas a cm., si: 1 milla = 1.60935 Km.1 pulgada = 2.534 cm

'''

'''
Dtos de entrada : Tenemos como datos de entradas el dato que 1 milla = 1.60935 y 1 pulgada = 2.534, Luego los dos valores que ingresa el usuario

Proceso : Se multiplca el valor ingresado por el usuario * con el valor preestablecido.

Dtos de salida : Las unidades convertidas de millas a KM y de pulgadas a CM
'''

PULGADA = 2.534
MILLA = 1.60935

num_km = float(input('Ingrese el número para pasar a KM'))
num_cm = float(input('Ingrese el número para pasar a CM'))

num_km *= MILLA
num_cm *= PULGADA

print(f'El número corresponde a {num_km} KM.')
print(f'El numero corresponde a {num_cm} CM.')