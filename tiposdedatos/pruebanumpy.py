import numpy as np
lista1= [1,2,3,4,5,6,7,8,9,0]
lista2= [0,9,8,7,6,5,4,3,2,1]
# print(type(lista1))

# array=np.array(lista1)
# print(type(array))

arr1=np.array(lista1)
arr2=np.array(lista2)

resultado1=np.add(arr1,arr2)
resultado2=np.subtract(arr1,arr2)
resultado3=np.multiply(arr1,arr2)
resultado4=np.divide(arr1,arr2)
print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)

data=np.array([1,2,3,4,5,6,7,8,98,7,6,5,4,3,2,1,0])
media=np.mean(data)
mediana=np.median(data)
desviacionestandar=np.std(data)
print(media)
print(mediana)
print(desviacionestandar)
