class Deuda:
    interes = 0.05
    def __init__(self, concepto, cantidad_deuda, pago_mensual):
        self.concepto = concepto
        self.cantidad_deuda = cantidad_deuda
        self.pago_mensual = pago_mensual

    def reducir_deuda(self, cantidad_pagada):
        self.cantidad_deuda -= cantidad_pagada
        return self.cantidad_deuda

    def pagar_deuda(self, deuda):
        if self.cuenta.retirar(deuda.pago_mensual):
            deuda_restante = deuda.reducir_deuda(deuda.pago_mensual)
            return f"{self.nombre} ha pagado la cuota de '{deuda.concepto}': -{deuda.pago_mensual}€. Deuda restante: {deuda_restante}€."
        else:
            return f"{self.nombre} no tiene saldo suficiente ({self.cuenta.saldo}€) para pagar la cuota de '{deuda.concepto}'."
