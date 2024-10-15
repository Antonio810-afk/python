class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f'Depósito de {cantidad} realizado. Nuevo saldo: {self.saldo}.')
        else:
            print('La cantidad a depositar debe ser mayor que cero.')

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f'Retiro de {cantidad} realizado. Nuevo saldo: {self.saldo}.')
        else:
            print('Fondos insuficientes o cantidad inválida.')

    def consultar_saldo(self):
        print(f'Saldo actual: {self.saldo}')

def main():
    cuentas = {}

    while True:
        print("\n1. Crear cuenta")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Consultar saldo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titular = input("Ingrese el nombre del titular: ")
            saldo_inicial = float(input("Ingrese el saldo inicial (0 si no desea): "))
            cuentas[titular] = CuentaBancaria(titular, saldo_inicial)
            print(f'Cuenta creada para {titular}.')

        elif opcion == '2':
            titular = input("Ingrese el nombre del titular: ")
            if titular in cuentas:
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                cuentas[titular].depositar(cantidad)
            else:
                print('Titular no encontrado.')

        elif opcion == '3':
            titular = input("Ingrese el nombre del titular: ")
            if titular in cuentas:
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                cuentas[titular].retirar(cantidad)
            else:
                print('Titular no encontrado.')

        elif opcion == '4':
            titular = input("Ingrese el nombre del titular: ")
            if titular in cuentas:
                cuentas[titular].consultar_saldo()
            else:
                print('Titular no encontrado.')

        elif opcion == '5':
            print('Saliendo del programa.')
            break

        else:
            print('Opción no válida, intente de nuevo.')

if __name__ == "__main__":
    main()
