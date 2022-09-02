
def maxi(*l): #*l trata los datos introducidos como un array
    if len(l) == 0:
        return 0

    m = l[0]# se declara l[0] como el mayor

    for ix in range(1,len(l)):#se recorre l desde la posición 1 hasta el final
        if l[ix] > m:# si l[ix] es mayor que el contenido de la primera posición l[0] 
            m = l[ix]# iguala a la variable "m"

    return m

def mini(*l):
    if len(l) == 0:
        return 0
    
    m = l[0]

    for ix in range(1,len(l)):
        if l[ix] < m: #si l[ix] es menor que el contenido de la primera posición de l[0]
            m = l[ix]
    
    return m

def media(*l):
    if len(l) == 0:
        return 0

    suma = 0
    for valor in l:
        suma += valor

    return suma / len(l)

funciones = {
    'max':maxi,
    'min':mini,
    'med':media
}

def returnF(nombre):
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]

print(maxi(1,3,-1,15,9))
print(mini(1,3,-1,15,9))
print(media(1,3,-1,15,9))
print("--------------------------------------")
print(returnF('max')(1,3,-1,15,9))
print(returnF('min')(1,3,-1,15,9))
print(returnF('med')(1,3,-1,15,9))
