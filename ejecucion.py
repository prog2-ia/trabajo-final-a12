from cuenta_bancaria import CuentaBancaria
from agente_financiero import AgenteFinanciero
from Deuda import Deuda
from Adulto import Adulto
from Ahorro import Ahorro
from agente_financiero import AgenteFinanciero
from madre_asesora import MadreAsesora
from padre import Padre
from Hijo import Hijo
if __name__ == '__main__':
    print("\nPRUEBAS INICIALES")
    prueba_cuenta=CuentaBancaria("renato",30_000)
    renato = Adulto("renato","sanchez","muñoz",41,550,prueba_cuenta,1800)

    vacaciones= Ahorro("vacaciones de verano",2000)
    vacaciones.aportar(prueba_cuenta,23.3)

    print(renato.cobrar_nomina())
    print(renato.comprar(1000,"frigorifico"))

    print("\nPRUEBA DE AGENTE FINANCIERO")
    cuenta_juan = CuentaBancaria("Juan Perez", 10000)
    agente = AgenteFinanciero("Juan","Perez","García",40,500,cuenta_juan,2500)
    print(agente.cobrar_nomina())
    agente.realizar_transaccion(200)
    agente.realizar_inversión(300)

    print("\nPRUEBA MADRE ASESORA")
    mi_cuenta = CuentaBancaria("Ana López", 5000)
    ana = MadreAsesora("Ana", "López", "García", 42, 800, mi_cuenta, 3000)
    ana.realizar_inversión(1000)
    print(ana.realizar_tarea_diaria())

    print("\nPRUEBA MADRE")
    mi_cuenta = CuentaBancaria("Ana López", 5000)
    ana = MadreAsesora("Ana", "López", "García", 42, 800, mi_cuenta, 3000)
    ana.realizar_inversión(1000)
    print(ana.cobrar_nomina())
    ana.dinero_ahorrado = 500
    print(ana.generar_intereses(0.02))
    print (ana.realizar_tarea_diaria())

    print("\nPRUEBA PADRE")
    cuenta_de_pepe = CuentaBancaria("Pepe Soto", 1000)
    papa_pepe = Padre("Pepe", "Soto", "Real", 48, 600, cuenta_de_pepe, 2200)
    print(papa_pepe.trabajo_extra(10, 25))
    print(papa_pepe.realizar_tarea_diaria())

    print("\nPRUEBA HIJO")
    cuenta_luis = CuentaBancaria("Luis Soto", 100)
    hijo_luis = Hijo("Luis", "Soto", "López", 10, 20, cuenta_luis, "Colegio Las Rozas", paga=15)
    print(hijo_luis.comprar(50, "videojuegos +18"))
    print(hijo_luis.comprar(5, "Balón de fútbol"))
    print(hijo_luis.realizar_tarea_diaria())
    print(hijo_luis.hacer_deberes("Mates"))
    print(hijo_luis.pedir_paga())
    print(renato.dar_paga(hijo_luis, 30))
