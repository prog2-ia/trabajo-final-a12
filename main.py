from cuenta_bancaria import CuentaBancaria
from Hijo import Hijo
from agente_financiero import AgenteFinanciero


def menu():
    # 1. Recogida de datos inicial para crear el objeto
    print("CREACIÓN DE PERFIL DE USUARIO")
    nombre = input("Nombre: ")
    apellidos = input("Apellido: ")

    try:
        saldo_inicial = float(input("Saldo inicial en cuenta (€): "))
        salario = float(input("Salario mensual (€): "))
    except ValueError:
        print("Error: Se asignarán valores por defecto (1000€ saldo / 1500€ salario).")
        saldo_inicial = 1000.0
        salario = 1500.0

    # 2. Inicialización de objetos
    cuenta = CuentaBancaria(f"Cuenta de {nombre}", saldo_inicial)
    usuario = AgenteFinanciero(nombre, apellido, "", 30, 500, cuenta, salario)

    print(f"\nUsuario {usuario.nombre} creado correctamente.")

    # 3. Bucle interactivo
    while True:
        print(f"\n[Día: {usuario.dias_trabajados}/30] | Saldo actual: {usuario.cuenta.saldo}€")
        print("1. Ir a trabajar (Avanzar 1 día)")
        print("2. Dar paga al hijo (20€)")
        print("3. Realizar inversión (Riesgo aleatorio)")
        print("4. Ver detalles del perfil")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        try:
            if opcion == "1":
                # El método realizar_tarea_diaria ya gestiona el cobro al llegar a 30
                print(usuario.realizar_tarea_diaria())

                if usuario.dias_trabajados >= 30:
                    usuario.dias_trabajados = 0
                    print("¡Nómina ingresada con éxito!")

            elif opcion == "2":
                # Creamos un Hijo para la prueba de transferencia
                hijo_prueba = Hijo("Luis", "Soto", "López", 10, 20, CuentaBancaria("Luis", 0), "Colegio Local")
                print(usuario.dar_paga(hijo_prueba, 20))

            elif opcion == "3":
                monto = float(input("¿Cuánto dinero quieres invertir?: "))
                # Ejecuta la lógica de inversión del agente
                usuario.realizar_inversión(monto)

            elif opcion == "4":
                print("\nINFORMACIÓN DEL PERFIL")
                print(f"Titular: {usuario}")  # Usa el __str__ de Familiar
                print(f"Salario: {usuario.salario}€")
                print(f"Días trabajados este mes: {usuario.dias_trabajados}")

            elif opcion == "5":
                print("Cerrando el simulador.")
                break

            else:
                print("Opción no válida.")

        except ValueError:
            print("Error: Introduce un número válido.")


if __name__ == "__main__":
    menu()