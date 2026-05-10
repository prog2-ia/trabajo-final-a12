from cuenta_bancaria import CuentaBancaria
from Hijo import Hijo
from Adulto import Adulto
from padre import Padre
from Madre import Madre
from agente_financiero import AgenteFinanciero
from madre_asesora import MadreAsesora


def menu():
    print("SIMULADOR DE ECONOMÍA FAMILIAR")

    #Creación del Personaje Principal
    nombre = input("Nombre: ")
    apellido1 = input("Primer Apellido: ")
    apellido2 = input("Segundo Apellido: ")

    try:
        edad = int(input("Edad: "))
        saldo_inicial = float(input("Saldo inicial en cuenta (€): "))
        salario = float(input("Salario mensual (€): "))
    except ValueError:
        print("Dato inválido. Usando valores por defecto.")
        edad, saldo_inicial, salario = 40, 1000.0, 1500.0

    cuenta_principal = CuentaBancaria(f"Cuenta de {nombre}", saldo_inicial)

    print("\nSelecciona tu rol:")
    print("1. Padre (Puede hacer trabajos extra)")
    print("2. Madre (Genera intereses)")
    print("3. Agente Financiero (Inversiones de riesgo)")
    print("4. Madre Asesora (Híbrido: Intereses + Inversiones)")

    rol = input("Rol: ")

    if rol == "1":
        usuario = Padre(nombre, apellido1, apellido2, edad, 500, cuenta_principal, salario)
    elif rol == "2":
        usuario = Madre(nombre, apellido1, apellido2, edad, 500, cuenta_principal, salario)
    elif rol == "3":
        usuario = AgenteFinanciero(nombre, apellido1, apellido2, edad, 500, cuenta_principal, salario)
    elif rol == "4":
        usuario = MadreAsesora(nombre, apellido1, apellido2, edad, 500, cuenta_principal, salario)
    else:
        print("Rol no reconocido, serás un Adulto estándar.")
        usuario = Adulto(nombre, apellido1, apellido2, edad, 500, cuenta_principal, salario)

    # 2. Creación del Hijo (Opcional pero recomendado para probar dar_paga)
    print("\nCreación del Hijo")
    nombre_h = input("Nombre del hijo/a: ")
    cuenta_hijo = CuentaBancaria(f"Cuenta de {nombre_h}", 0)
    mi_hijo = Hijo(nombre_h, apellido1, apellido2, 10, 50, cuenta_hijo, "Colegio Público", paga=20)

    #Bucle interactivo
    while True:
        print(f"\nESTADO")
        print(f"Usuario: {usuario} | Saldo: {usuario.cuenta.saldo}€")
        print(f"Hijo: {mi_hijo.nombre} | Saldo Hijo: {mi_hijo.cuenta.saldo}€ | Ahorro Hijo: {mi_hijo.dinero_ahorrado}€")
        print(f"Progreso Mes: {usuario.dias_trabajados}/30 días")
        print("-" * 20)

        print("1. Ir a trabajar (Avanzar día)")
        print("2. Dar paga al hijo")
        print("3. Acciones Especiales (Según tu Rol)")
        print("4. Ver detalles del perfil")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        try:
            if opcion == "1":
                resultado = usuario.realizar_tarea_diaria()
                print(resultado)
                # Reiniciar contador si ya cobró
                if "ha ingresado su salario" in resultado:
                    usuario.dias_trabajados = 0

            elif opcion == "2":
                cantidad = float(input("¿Cuánto le das de paga?: "))
                print(usuario.dar_paga(mi_hijo, cantidad))
                # El hijo también puede usar su método de recibir paga
                print(mi_hijo.pedir_paga())

            elif opcion == "3":
                print("\nACCIONES ESPECIALES")
                if isinstance(usuario, Padre):
                    horas = int(input("¿Cuántas horas extra has trabajado?: "))
                    print(usuario.trabajo_extra(horas))

                elif isinstance(usuario, MadreAsesora):
                    print("1. Invertir (Agente) | 2. Generar Intereses (Madre)")
                    sub = input("Elige: ")
                    if sub == "1":
                        monto = float(input("Cantidad a invertir: "))
                        usuario.realizar_inversión(monto)
                    else:
                        usuario.dinero_ahorrado = float(
                            input("¿Cuánto dinero tienes en el 'calcetín' para intereses?: "))
                        print(usuario.generar_intereses())

                elif isinstance(usuario, AgenteFinanciero):
                    monto = float(input("Cantidad a invertir: "))
                    usuario.realizar_inversión(monto)

                elif isinstance(usuario, Madre):
                    usuario.dinero_ahorrado = float(input("¿Cuánto dinero tienes ahorrado aparte?: "))
                    print(usuario.generar_intereses())
                else:
                    print("Tu personaje no tiene acciones especiales.")

            elif opcion == "4":
                print(f"\nDETALLES:")
                print(f"Nombre completo: {usuario}")
                print(f"Tipo de clase: {type(usuario).__name__}")
                print(f"Salario base: {usuario.salario}€")

            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida.")

        except ValueError as e:
            print(f"Error de entrada: {e}")


if __name__ == "__main__":
    menu()