class Deuda:
    def __init__(self,cantidad_deuda,interes,pago_mensual):
        self.cantidad_deuda=cantidad_deuda
        self.interes = interes
        self.pago_mensual=pago_mensual
    def deuda_restante(self,numero_pagos):
        self.numero_pagos = numero_pagos
        return self.cantidad_deuda - (self.pago_mensual*self.numero_pagos)
casa = Deuda(100_000,0.05,650)
print(casa.deuda_restante(5))