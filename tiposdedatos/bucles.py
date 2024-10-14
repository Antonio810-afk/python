tamaño=input ("ingrese el tamaño de la lista")
lista=[]
for i in range(int(tamaño)):
    print(f"el valor a ingresar es {i}")
    valor=input()
    lista.append(valor)
print(lista)
