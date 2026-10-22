from excecoes import SaldoInsuficienteError


class ContaBancaria:
    def __init__(self, nome_do_titular):
        self.nome_do_titular = nome_do_titular
        self.saldo = 0
        self.operacoes = []

    def depositar(self, valor):
        if valor <= 0:
            return "Valor Incorreto, deposito não efetuado!"
        self.saldo += valor
        self.operacoes.append(f"Depósito: +R${valor:.2f}")
        return f"Seu novo saldo é R${self.saldo:.2f}"

    def sacar(self, valor):
        if valor <= 0:
            return "Valor para saque inválido."
        if valor > self.saldo:
            raise SaldoInsuficienteError(valor, self.saldo)
        self.saldo -= valor
        self.operacoes.append(f"Saque: -R${valor:.2f}")
        return f"Saque bem-sucedido; seu novo saldo é R${self.saldo:.2f}"

    def extrato(self):
        print(f"Titular : {self.nome_do_titular}")
        print(f"Seu saldo é R${self.saldo:.2f}")
        for operacao in self.operacoes:
            print(operacao)
