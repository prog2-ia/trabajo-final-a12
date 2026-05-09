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

import os
import pickle
def guardar_datos(objeto, nombre_archivo):
    # Corregido: Ahora verificamos si existe la carpeta
    if not os.path.exists('datos'):
        os.makedirs('datos')
    ruta = os.path.join('datos', f"{nombre_archivo}.dat")
    with open(ruta, 'wb') as f:
        pickle.dump(objeto, f)

