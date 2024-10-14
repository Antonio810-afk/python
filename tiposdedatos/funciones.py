#def saludar():
#    print ("hola mundo")
#saludar()

#cantidad=int(input ("ingrese la cantidad del producto"))
#precio=int(input ("ingrese el valor del producto"))

#def multiplicar(a,b):
#    return a*b

#total= multiplicar(cantidad,precio)
#print(total)

def calcular(a,b):
    return a*b
def multiplicar(a,b):
    return a*b

total=0
cantidad=1

while cantidad!=0:
    print("ingrese cantidad del producto")
    cantidad=float(input())
    if cantidad==0:
        break
    print("ingrese valor del producto")
    valor=float(input())
    subtotal=calcular(cantidad,valor)
    Subtotal=multiplicar(subtotal,1.19)
    total+=Subtotal
print(f"el total de los productos es {total}")
