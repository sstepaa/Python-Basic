ag030bf = []
#Como cargar un array
ag030bf = ['vw1500' ,'fitito', 'mb' , 'audi' , 'ford' , 'r12' , 'fiat', 'clio' , 504 , 'falcon']
#mostrar
#print(ag030bf)

#La mejor forma de mostrar el vector es dentro de un for
#De esta manera el elemento va a recorrer posicion por posicion el vector
for elemento in ag030bf :
    print(elemento)
#Agregar en la pizarra append(agrega) , remove(elimina elementos) , pop(elimina x posicion) , insert(inserta) , reverse(Invierte el vector)
#Ultima posicion N -1
#Si vos le queres agregar mas elementos
ag030bf.append(input('Ingrese un dato'))
print(ag030bf)
#Hay que decir donde y que quiero hacer esa insercion
ag030bf.insert(1 , input('Ingrese un elemento a insertar'))
print(ag030bf)

#Si quiero eliminar un elemento pop elimina por posicion
ag030bf.pop(4)
print(ag030bf)
#Elimina todos los r12 que teniamos en nuestro vector
for elemento in ag030bf:
    if elemento == 'r12':
        ag030bf.remove('r12')

#ag030bf.remove('r12')
print(ag030bf)

#Quiero saber si tengo un elemento en el vector.
i = 0 
while i < len(ag030bf) and ag030bf[i] != 'volvo':
    i += 1
print(i)
if i == len(ag030bf) :
    print('No encontre el elemento')
else:
    print(f'Esta en la posicion{i}')