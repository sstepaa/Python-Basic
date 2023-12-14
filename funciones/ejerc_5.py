'''
Ejercicio 2

Cargar un arreglo con letras hasta que se lea "FIN". Una vez cargado el arreglo se pide:

calcular la cantidad de vocales discriminado por vocal
generar dos arreglos: uno que contengan las letras y en otro las cantidades que aparecen cada letra (en el arreglo de letras no se deben repetir las mismas letras).
insertar antes de cada cantidad igual a 1 un cero (0) en el arreglo de cantidades y un "-" en el arreglo de letras
eliminar del arreglo original todas las vocales.
ordenar los arreglos del punto 3 por cantidad de apariciones.

'''

def cargar(vec):
    i = 0
    elemento = str(input('Ingresa una palabra'))
    while elemento != 'FIN' : 
        vec.append(elemento)
        
        elemento = str(input('Ingresa una palabra'))
        i += 1
        
def contadorVocales(vec):
    vocales = ['a' , 'e' , 'i' , 'o' , 'u']
    cuenta_a = cuenta_e = cuenta_i = cuenta_o = cuenta_u = 0
    
    for palabra in vec : 
        for letra in palabra : 
            letra = letra.lower()
            
            if letra == 'a' : 
                cuenta_a += 1
            elif letra == 'e' : 
                cuenta_e += 1 
            elif letra == 'i':
                cuenta_i += 1
            elif letra == 'o':
                cuenta_o += 1
            elif letra == 'u':
                cuenta_u += 1
            
    print(f'Vocal a: {cuenta_a}')
    print(f'Vocal e: {cuenta_e}')
    print(f'Vocal i: {cuenta_i}')
    print(f'Vocal o: {cuenta_o}')
    print(f'Vocal u: {cuenta_u}')
    
def contar_letras(vec):
    letras = []
    cantidades = []
    texto =''.join(vec)
    
    for letra in texto:
        letra = letra.lower()
        if letra not in letras : 
            letras.append(letra)
            cantidades.append(1)
        else : 
            index = letras.index(letra)
            cantidades[index] += 1
            
    return letras , cantidades



vector_a = []
cargar(vector_a)
letras , cantidades = contar_letras(vector_a)
contadorVocales(vector_a)

print(vector_a)
print('Letras unicas en el texto')
print(letras)
for letra , cantidad in zip(letras , cantidades):
    print(f'letra: {letra} , cantidad : {cantidad}')


