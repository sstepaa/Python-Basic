#Como se usa la funcion REMOVE.
#Siempre se tiene que utilizar en un while , debido a que se modifica el len del vector que estamos recorriendo , en el cual si se usa un for , este len nunca se actualiza es estatico y conlleva un error.
#El remove Elimina la primera ocurrencia que encuentra del parametro.
#Eliminar si hay numeros 3 en el vector
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
             vec.remove(num)
        else:
            i += 1
            
#Programa general
vec = []
carga(vec)
print(vec)

numDelete = int(input('Ingresa el numero que deseas eliminar'))
eliminar(vec , numDelete)
print(vec)