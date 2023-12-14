#Como se usa la funcion POP.
#Siempre se tiene que utilizar en un while , debido a que se modifica el len del vector que estamos recorriendo , en el cual si se usa un for , este len nunca se actualiza es estatico y conlleva un error.
#El pop elimina por posicion pasada(INDICE)

def carga(vec):
    i = 0 
    num = int(input('Ingresa un numero'))
    while num != 0:
        vec.append(num)
        
        num = int(input('Ingresa un numero'))
        i += 1
        
def eliminar(vec , num):
    i = 0
    while i < len(vec):
        if vec[i] == num:
             vec.pop(num - 1)#Elimina por posicion y el indice inicia en 0 por eso restamos uno
        else:
            i += 1
            
#programa principal
vec = []
carga(vec)
print(vec)

numPos = int(input('Ingrese la posicion que quiere eliminar del vector'))
while numPos <= 0 or numPos > len(vec):
    print('Error de posicion , no existe esa posicion en el vector')
    
    numPos = int(input('Ingrese la posicion que quiere eliminar del vector'))

eliminar(vec , numPos)
print(vec)