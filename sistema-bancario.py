class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('O valor de depósito deve ser positivo.')

    def sacar(self, valor):
        if valor <= 0:
            print('O valor de saque deve ser positivo.')
        elif len(self.saques) >= 3:
            print('Limite diário de saques atingido.')
        elif valor > 500:
            print('Limite máximo de R$ 500,00 por saque.')
        elif valor > self.saldo:
            print('Saldo insuficiente para realizar o saque.')
        else:
            self.saldo -= valor
            self.saques.append(valor)
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')

    def extrato(self):
        print('Extrato:')
        for deposito in self.depositos:
            print(f'Depósito: R$ {deposito:.2f}')
        for saque in self.saques:
            print(f'Saque: R$ {saque:.2f}')
        print(f'Saldo atual: R$ {self.saldo:.2f}')
        if not self.depositos and not self.saques:
            print('Não foram realizadas movimentações.')

# Instanciando o sistema bancário
sistema = SistemaBancario()

sistema.depositar(1000)
sistema.sacar(300)
sistema.sacar(700)
sistema.sacar(500)
sistema.depositar(500)
sistema.extrato()