class Deuda:
    interes = 0.05
    def __init__(self,cantidad_deuda,pago_mensual):
        self.cantidad_deuda=cantidad_deuda
        self.pago_mensual=pago_mensual
    def deuda_restante(self,numero_pagos):
        self.numero_pagos = numero_pagos
        if CuentaBancaria.cantidad >= self.pago_mensual:
            return self.cantidad_deuda - (self.pago_mensual*self.numero_pagos)
        else:
            print("Cantidad insuficiente")
casa = Deuda(100_000,650)
print(casa.deuda_restante(5))
# arreglando un commit