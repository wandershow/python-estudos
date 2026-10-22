class SaldoInsuficienteError(Exception):
    """Exception raised when a withdrawal exceeds the available balance."""

    def __init__(self, valor_saque, saldo_disponivel):
        self.valor_saque = valor_saque
        self.saldo_disponivel = saldo_disponivel
        super().__init__(self.__str__())

    def __str__(self):
        return (
            f"Saldo insuficiente: tentativa de saque de R${self.valor_saque:.2f}; "
            f"saldo disponível R${self.saldo_disponivel:.2f}."
        )
