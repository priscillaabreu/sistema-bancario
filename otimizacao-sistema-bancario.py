class SistemaBancario:
    def __init__(self):
        self.usuarios = []
        self.contas = []

    def criar_usuario(self, nome, data_nascimento, cpf, endereco):
        for usuario in self.usuarios:
            if usuario['cpf'] == cpf:
                return "CPF já cadastrado"
        self.usuarios.append({
            'nome': nome,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'endereco': endereco
        })
        return "Usuário criado com sucesso"

    def criar_conta(self, usuario):
        numero_conta = len(self.contas) + 1
        self.contas.append({
            'agencia': '0001',
            'numero_conta': numero_conta,
            'usuario': usuario,
            'saldo': 0,
            'extrato': []
        })
        return f"Conta criada com sucesso. Número da conta: {numero_conta}"

    def depositar(self, *, saldo, valor, extrato):
        if valor > 0:
            saldo += valor
            extrato.append(f'Depósito de R$ {valor:.2f}')
            return saldo, extrato
        else:
            return saldo, extrato

    def sacar(self, *, saldo, valor, extrato, limite, numero_saques, limite_saques):
        if valor <= 0:
            return saldo, extrato
        elif len(extrato) >= limite_saques:
            return saldo, extrato
        elif valor > 500:
            return saldo, extrato
        elif valor > saldo:
            return saldo, extrato
        else:
            saldo -= valor
            extrato.append(f'Saque de R$ {valor:.2f}')
            numero_saques += 1
            return saldo, extrato

    def extrato(self, saldo, *, extrato):
        return saldo, extrato

# Instanciando o sistema bancário
sistema = SistemaBancario()

while True:
    print("\n-- Menu --")
    print("1. Criar Usuário")
    print("2. Criar Conta")
    print("3. Realizar Depósito")
    print("4. Realizar Saque")
    print("5. Visualizar Extrato")
    print("6. Visualizar Usuários")
    print("7. Visualizar Contas")
    print("8. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento do usuário: ")
        cpf = input("Digite o CPF do usuário: ")
        endereco = input("Digite o endereço do usuário (logradouro, nro - bairro - cidade/sigla estado): ")
        mensagem_usuario = sistema.criar_usuario(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
        print(mensagem_usuario)
    elif escolha == "2":
        cpf = input("Digite o CPF do usuário para criar a conta: ")
        mensagem_conta = sistema.criar_conta(usuario=cpf)
        print(mensagem_conta)
    elif escolha == "3":
        numero_conta = int(input("Digite o número da conta: "))
        valor = float(input("Digite o valor a ser depositado: "))
        for conta in sistema.contas:
            if conta['numero_conta'] == numero_conta:
                saldo, extrato = sistema.depositar(saldo=conta['saldo'], valor=valor, extrato=conta['extrato'])
                conta['saldo'] = saldo
                conta['extrato'] = extrato
                print(f'Depósito de R$ {valor:.2f} realizado na conta {numero_conta}.')
                break
        else:
            print(f'Conta {numero_conta} não encontrada.')
    elif escolha == "4":
        numero_conta = int(input("Digite o número da conta: "))
        valor = float(input("Digite o valor a ser sacado: "))
        for conta in sistema.contas:
            if conta['numero_conta'] == numero_conta:
                saldo, extrato = sistema.sacar(saldo=conta['saldo'], valor=valor, extrato=conta['extrato'], limite=3, numero_saques=0, limite_saques=3)
                conta['saldo'] = saldo
                conta['extrato'] = extrato
                print(f'Saque de R$ {valor:.2f} realizado na conta {numero_conta}.')
                break
        else:
            print(f'Conta {numero_conta} não encontrada.')
    elif escolha == "5":
        numero_conta = int(input("Digite o número da conta: "))
        for conta in sistema.contas:
            if conta['numero_conta'] == numero_conta:
                saldo, extrato = sistema.extrato(saldo=conta['saldo'], extrato=conta['extrato'])
                print(f'Extrato da conta {numero_conta}:')
                for movimento in extrato:
                    print(movimento)
                print(f'Saldo atual: R$ {saldo:.2f}')
                break
        else:
            print(f'Conta {numero_conta} não encontrada.')
    elif escolha == "6":
        print("\n-- Usuários --")
        for usuario in sistema.usuarios:
            print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}")
    elif escolha == "7":
        print("\n-- Contas --")
        for conta in sistema.contas:
            print(f"Conta: {conta['numero_conta']}, Agência: {conta['agencia']}, CPF do Titular: {conta['usuario']}")
    elif escolha == "8":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Escolha novamente.")