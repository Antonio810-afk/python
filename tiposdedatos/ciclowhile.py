tamaño=int (input ("ingrese el tamaño de la lista"))
lista=[]
while tamaño != 0:
    tamaño-=1
    print(f"el valor al ingresar es: {tamaño}")
    valor=input()
    lista.append(valor)
print(lista)
