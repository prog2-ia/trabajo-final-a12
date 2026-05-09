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
    if not os.path.exists('datos'):
        os.makedirs('datos')
    ruta = os.path.join('datos', f"{nombre_archivo}.dat")
    with open(ruta, 'wb') as f:
        pickle.dump(objeto, f)

def cargar_datos(nombre_archivo):
    ruta = os.path.join('datos', f"{nombre_archivo}.dat")
    if os.path.exists(ruta):
        with open(ruta, 'rb') as f:
            return pickle.load(f)
    return None

cuenta = cargar_datos("cuenta_principal") or CuentaBancaria("Familia", 1000)

elif opcion == "5":
            try:
                cantidad = float(input("Cantidad a invertir: "))
                usuario.realizar_inversión(cantidad)
            except ValueError:
                # Gestionamos el error de tipo de dato
                print("Error: Introduce un valor numérico válido.")

from Hijo import Hijo
        elif opcion == "6":
            hijo = Hijo("Luis", "Perez", "Gomez", 10, 0, CuentaBancaria("Luis", 0), "Colegio")
            print(usuario.dar_paga(hijo, 20))

