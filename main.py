from cuenta_bancaria import CuentaBancaria
from Adulto import Adulto

def menu():
    print("BIENVENIDO AL SISTEMA FAMILIAR")
    # Creamos una cuenta y un usuario de prueba
    cuenta = CuentaBancaria("Familia Test", 500)
    usuario = Adulto("Juan", "Perez", "Gomez", 40, 600, cuenta, 1500)

    while True:
        print("\n1. Ver Saldo\n2. Salir")
        opcion = input("Selecciona: ")
        if opcion == "1":
            print(f"Saldo: {usuario.cuenta.saldo}") # Acceso a cuenta
        elif opcion == "2":
            break

if __name__ == "__main__":
    menu()
    elif opcion == "3":
        print(usuario.realizar_tarea_diaria())
    elif opcion == "4":
        print(usuario.cobrar_nomina())

def guardar_datos(cuenta):
    with open("datos/cuenta.dat", "wb") as f: #Error si la carpeta 'datos' no existe
        pickle.dump(cuenta, f)