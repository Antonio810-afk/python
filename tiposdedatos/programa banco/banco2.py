class Cliente:
    def __init__(self, nombre, apellido, edad, telefono, saldo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.saldo = saldo

    def __str__(self):
        return (f'Nombre: {self.nombre} {self.apellido}, Edad: {self.edad}, '
                f'Teléfono: {self.telefono}, Saldo: {self.saldo}')


class SistemaClientes:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, nombre, apellido, edad, telefono, saldo):
        cliente = Cliente(nombre, apellido, edad, telefono, saldo)
        self.clientes.append(cliente)
        print(f'Cliente {nombre} {apellido} agregado.')

    def eliminar_cliente(self, telefono):
        for cliente in self.clientes:
            if cliente.telefono == telefono:
                self.clientes.remove(cliente)
                print(f'Cliente con teléfono {telefono} eliminado.')
                return
        print('Cliente no encontrado.')

    def listar_clientes(self):
        if self.clientes:
            print("\nLista de Clientes:")
            for cliente in self.clientes:
                print(cliente)
        else:
            print('No hay clientes en el sistema.')

    def consultar_cliente(self, telefono):
        for cliente in self.clientes:
            if cliente.telefono == telefono:
                print(cliente)
                return
        print('Cliente no encontrado.')


def main():
    sistema = SistemaClientes()

    while True:
        print("\n1. Agregar Cliente")
        print("2. Eliminar Cliente")
        print("3. Listar Clientes")
        print("4. Consultar Cliente")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del cliente: ")
            apellido = input("Ingrese el apellido del cliente: ")
            edad = input("Ingrese la edad del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            saldo = input("Ingrese el saldo del cliente: ")
            sistema.agregar_cliente(nombre, apellido, edad, telefono, saldo)

        elif opcion == '2':
            telefono = input("Ingrese el teléfono del cliente a eliminar: ")
            sistema.eliminar_cliente(telefono)

        elif opcion == '3':
            sistema.listar_clientes()

        elif opcion == '4':
            telefono = input("Ingrese el teléfono del cliente a consultar: ")
            sistema.consultar_cliente(telefono)

        elif opcion == '5':
            print('Saliendo del programa.')
            break

        else:
            print('Opción no válida, intente de nuevo.')

if __name__ == "__main__":
    main()
