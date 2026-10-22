from excecoes import SaldoInsuficienteError
from conta import ContaBancaria

conta = ContaBancaria("Wanderson")
conta.depositar(200)
conta.sacar(50)

try:
    conta.sacar(500)
except SaldoInsuficienteError as erro:
    print(f"Erro: {erro}")

conta.extrato()
