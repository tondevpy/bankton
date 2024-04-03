contas = []

def criarConta():
    nome = input('\033[96mInforme o nome da conta: \033[0m')
    if nome:
        for conta in contas:
            if nome == conta['nome']:
                print('\033[91mConta existente, não é possível criar conta com o mesmo nome!\033[0m')
                return
            
        
        usuario = {
            'id': len(contas) + 1,
            'nome': nome,
            'saldo': 0
        }
        contas.append(usuario)
        print('\033[92mConta criada com sucesso\033[0m')

    
    else:
        print('\033[93mFavor preencha o campo nome para criar a conta\033[0m')

def deposito():
    nome = input('\033[96mInforme o nome da conta: \033[0m')
    if nome:
        for conta in contas:
            if nome == conta['nome']:
                print('Conta localizada!')
                valor = input('\033[96mInforme o valor do depósito: \033[0m').replace(',','.')
                if valor:
                    novoValor = valor.replace(',','.')
                    novoValor = float(novoValor)
                    conta['saldo'] += novoValor
                    print('\033[92mDeposito realizado com sucesso\033[0m')

                else:
                    print('\033[91mInformou um valor inválido!\033[0m')
            else:
                print('\033[91mConta não localizada!\033[0m')


def saque():
    nome = input('\033[96mInforme o nome da conta: \033[0m').lower()
    if nome:
        for conta in contas:
            if conta['nome'] == nome:
                print('Usuário encontrado')
                saldo = conta['saldo']
                saque = float(input('\033[96minforme o valor que deseja sacar: \033[0m'))
                if saque:
                    if saldo >= saque:
                        conta['saldo'] -= saque
                        print('\033[92mSaque realizado com sucesso\033[0m')
                    else:
                        print('\033[91mO valor disponível é inferior ao saque solicitado!\033[0m')
                else:
                    print('\033[91mInformou um valor inválido!\033[0m')
            else:
                print('\033[91mUsuário não localizado\033[0m')

def verificarConta():
    nome = input('\033[96mInforme o nome da conta: \033[0m').lower()
    if nome:
        for conta in contas:
            if conta['nome'] == nome:
                print('\033[92mConta localizada!\033[0m')
                break  # Encerra o loop assim que a conta é encontrada
        else:
            print('\033[91mConta não localizada\033[0m')
    else:
        print('\033[93mFavor preencher o campo nome!\033[0m')


def conferirSaldo():
    nome = input('\033[96mInforme o nome da conta: \033[0m').lower()
    if nome:
        for conta in contas:
            if conta['nome'] == nome:
                saldo = conta['saldo']
                print('\033[92mConta localizada! saldo disponível: R$' + str(saldo) + '\033[0m')
                print()
                break  # Encerra o loop assim que a conta é encontrada
        else:
            print('\033[91mConta não localizada\033[0m')
    else:
        print('\033[93mFavor preencher o campo nome!\033[0m')


print('\033[95mSeja bem vindo ao TonBank\033[0m')
while True:
    
    print('Escolha uma opção! \n\033[96m[1] - criar conta\n[2] - realizar um depósito\n[3] - realizar um saque\n[4] - verificar conta existente\n[5] - conferir saldo\n[6] - Sair\033[0m')
    try:
        opcao = input('\033[94mInforme a opção desejada: \033[0m')
        if opcao == '1':
            criarConta()
        elif opcao == '2':
            deposito()
        elif opcao == '3':
            saque()
        elif opcao == '4':
            verificarConta()
        elif opcao == '5':
            conferirSaldo()
        elif opcao == '6':
            print('\033[92mOperação finalizada com sucesso!\033[0m')
            break
    except:
        print('\033[91mEscolheu uma opção inválida!\033[0m')
