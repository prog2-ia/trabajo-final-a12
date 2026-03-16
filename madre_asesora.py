from Madre import Madre
from agente_financiero import AgenteFinanciero
class MadreAsesora(Madre, AgenteFinanciero):
    def __init__(self, nombre, apellido1, apellido2, edad, gastos_fijos, cuenta, salario ):
        Madre.__init__(self, nombre, apellido1, apellido2, edad, gastos_fijos,cuenta, salario)
        # pongo Madre porque en herencia multiple el super() suele dar error
