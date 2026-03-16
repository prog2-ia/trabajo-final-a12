from cuenta_bancaria import CuentaBancaria
from agente_financiero import AgenteFinanciero
from Deuda import Deuda
from Adulto import Adulto
from Ahorro import Ahorro
from agente_financiero import AgenteFinanciero
from madre_asesora import MadreAsesora
if __name__ == '__main__':
    prueba_cuenta=CuentaBancaria("renato",30_000)
    renato = Adulto("renato","sanchez","muñoz",41,550,prueba_cuenta,1800)
    vacaciones= Ahorro("vacaciones de verano",2000)
    vacaciones.aportar(prueba_cuenta,23.3)
    print(renato.cobrar_nomina())
    print(renato.comprar(1000,"frigorifico"))
    cuenta_juan = CuentaBancaria("Juan Perez", 10000)
    agente = AgenteFinanciero("Juan","Perez","García",40,500,cuenta_juan,2500)
    print(agente.cobrar_nomina())
    agente.realizar_transaccion(200)
    agente.realizar_inversión(300)
    mi_cuenta = CuentaBancaria("Ana López", 5000)
    ana = MadreAsesora("Ana", "López", "García", 42, 800, mi_cuenta, 3000)
    ana.realizar_inversión(1000)


