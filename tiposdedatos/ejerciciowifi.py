redes=[]


while True:
    print("opcion 1 agregar red")
    print("opcion 2 ver redes")
    print("opcion 0 para salir")
    opcion=int(input("ingrese una opcion"))

    if opcion==1:
        red={}
        print("ingrese la red")
        nombre=input()
        red["nombre"]=nombre
        print("ingrese la contraseña")
        clave=input()
        red["clave"]=clave
        redes.append(red)

    elif opcion==2:
        for i in range(len(redes)):
            print(redes[i])
