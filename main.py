import os
import pickle
from cuenta_bancaria import CuentaBancaria
from Adulto import Adulto
from Hijo import Hijo
from agente_financiero import AgenteFinanciero


def guardar_datos(objeto, nombre_archivo):4
    if not os.path.exists('datos'):
        os.makedirs('datos')
    ruta = os.path.join('datos', f"{nombre_archivo}.dat")
    with open(ruta, 'wb') as f:
        pickle.dump(objeto, f)


def cargar_datos(nombre_archivo):
    ruta = os.path.join('datos', f"{nombre_archivo}.dat")
    if os.path.exists(ruta):
        try:
            with open(ruta, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
    return None


def menu():
    print("SISTEMA DE GESTIÓN ECONÓMICA FAMILIAR")

    # Cargamos cuenta y usuario
    cuenta = cargar_datos("cuenta_principal")
    if not cuenta:
        cuenta = CuentaBancaria("Familia Principal", 1000)

    # Cargamos el progreso del usuario si existe, si no lo creamos
    usuario = cargar_datos("perfil_usuario")
    if not usuario:
        usuario = AgenteFinanciero("Juan", "Perez", "Gomez", 40, 600, cuenta, 2000)
    else:
        # Aseguramos que el usuario cargado use la cuenta cargada (vincular objetos)
        usuario.cuenta = cuenta

    while True:
        # Mostramos los días trabajados para que el usuario vea su progreso mensual
        print(f"\n[Día: {usuario.dias_trabajados}/30] | Usuario: {usuario.nombre} | Saldo: {usuario.cuenta.saldo}€")
        print("1. Ir a trabajar (Avanzar día)")
        print("2. Dar paga al hijo (20€)")
        print("3. Realizar inversión (Riesgo)")
        print("4. Ver información completa del perfil")
        print("5. Guardar y Salir")

        opcion = input("Selecciona una opción: ")

        try:
            if opcion == "1":
                # Al llegar a 30, el método realizar_tarea_diaria() ya llama a cobrar_nomina()
                print(usuario.realizar_tarea_diaria())

                if usuario.dias_trabajados >= 30:
                    usuario.dias_trabajados = 0
                    print("Comienza un nuevo mes laboral")

            elif opcion == "2":
                hijo = Hijo("Luis", "Perez", "Gomez", 10, 0, CuentaBancaria("Luis", 0), "Colegio")
                print(usuario.dar_paga(hijo, 20))

            elif opcion == "3":
                cantidad = float(input("¿Cuánto dinero quieres arriesgar?: "))
                usuario.realizar_inversión(cantidad)

            elif opcion == "4":
                # Uso del método __str__ (Aspecto 1: POO)
                print(f"\n FICHA DE {usuario.nombre.upper()}")
                print(usuario)
                print(f"Salario mensual: {usuario.salario}€")

            elif opcion == "5":
                # Guardamos tanto la cuenta y los dias trabajados
                guardar_datos(cuenta, "cuenta_principal")
                guardar_datos(usuario, "perfil_usuario")
                print("Datos guardados. ¡Buen día!")
                break
            else:
                print("Opción inválida.")

        except ValueError:
            print("Error: Entrada no válida. Introduce números para las cantidades.")


if __name__ == "__main__":
    menu()