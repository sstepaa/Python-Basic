'''
Cargar un arreglo de 15 elementos con las medidas del ancho de 15 terrenos rectangulares.
Luego cargar otro arreglo de 15 elementos con las medidas del fondo de los terrenos.
a) Hallar el arreglo superficie.Mostrarlo ordenado.
b) Hallar cuál es el ancho correspondiente al terreno de mayor fondo.


'''

def cargar(vec):
    for i in range(3):
        num = int(input('Ingrese las medidas'))
        vec.append(num)
        
def superficie(vecAncho , vecAlto , vec_S):
    for i in range(len(vecAncho)):
        super = vecAncho[i] * vecAlto[i]
        vec_S.append(super)

def maximo(vec1 , vec2):
    maximo = vec2[0]
    for i in range(len(vec1)):
        if maximo > vec1[i]:
            maximo = vec2[i]
    return maximo
    

def mostrar(msg , vec):
    print(' ')
    print(msg)
    for i in range(len(vec)):
        print(vec[i] , end=" ")

vec_A = []
vec_B = []
vec_Super = []

#Invocamos la funcion cargar
cargar(vec_A)
cargar(vec_B)
superficie(vec_A, vec_B, vec_Super)
maximo(vec_A, vec_B)
mostrar(' Vector con el ancho de los terrenos ' , vec_A)
mostrar('Vector con el alto de los terrenos ' , vec_B)
mostrar('La superficie de cada terreno es ' , vec_Super)
print(f'el ancho correspondiente al terreno de mayor fondo es {maximo}')
        