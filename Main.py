from ContaCorrente import Conta_Corrente
from ContaPoupanca import Conta_Poupanca



cliente_corrente = Conta_Corrente(Limite = 1000, Saldo=1000, IdConta=1)
cliente_poupanca = Conta_Poupanca(IdConta=2, Saldo=1500)

while True:

    print(' ______________________________________________')

    print('               SEJA BEM VINDO!                 |')

    print('_______________________________________________|') 
    
    print('|PRESSIONE 1 P/ CONSULTA DE SALDO DA CONTA     |')

    print('|PRESSIONE 2 PARA SAQUES                       |')
     
    print('|PRESSIONE 3 PARA DEPÓSITO                     |')
    
    print('|PRESSIONE 4 PARA EXIBIR EXTRATO               |')

    print('|PRESSIONE 5 PARA FAZER UMA SIMULAÇÃO          |')

    print('|PRESSIONE 0 PARA SAIR DO SISTEMA              |')

    print('|______________________________________________|')
          

    opcao = int(input('>> '))
    
    # sai do program
    if opcao == 0:  
        print('Obrigado pela preferencia! \nVolte sempre.')
        break
        

    # consulta saldo
    elif opcao == 1:
        tipo_conta = int(input("Indique qual tipo de conta você gostaria de usar: \nPRESSIONE 1 PARA CONTA POUPANÇA \nPRECIONE 2 PARA CONTA CORRENTE\n>> ")) 
        if tipo_conta == 1:
            print(f"Saldo: {cliente_poupanca.Get_Saldo()}")
        elif tipo_conta == 2:
            print(f"Saldo: {cliente_corrente.Get_Saldo()}")
        else:
            print("Valor invalido, tente novamente!")
        
    # realiza saque
    elif opcao == 2:
        
        valor_cliente = int(input("Digite o valor a ser sacado:"))

        tipo_conta = int(input("Indique qual tipo de conta você gostaria de usar: \nPRESSIONE 1 PARA CONTA POUPANÇA \nPRECIONE 2 PARA CONTA CORRENTE:\n>> "))

        if tipo_conta == 1:
            cliente_poupanca.sacar(valor=valor_cliente)
        elif tipo_conta== 2:
            cliente_corrente.sacar(valor=valor_cliente)
        else:
            print("Valor invalido, tente novamente!")

    # realiza depositos
    elif opcao == 3:
        valor_cliente = int(input("Digite o valor a ser depositado: "))

        tipo_conta = int(input("Indique qual tipo de conta você gostaria de usar: \nPRESSIONE 1 PARA CONTA POUPANÇA \nPRECIONE 2 PARA CONTA CORRENTE\n>>"))

        if tipo_conta == 1:
            cliente_poupanca.depositar(valor=valor_cliente)
            print(f'\nVocê Depositou R$ {valor_cliente:,.2f} na sua conta!')
        elif tipo_conta == 2:
            cliente_corrente.depositar(valor=valor_cliente)
            print(f'\nVocê Depositou R$ {valor_cliente:,.2f} na sua conta!')
        else:
            print("Valor invalido, tente novamente!")

    # extrato da conta
    elif opcao == 4:
        tipo_conta = int(input("Indique qual tipo de conta você gostaria de usar: \n PRESSIONE 1 PARA CONTA POUPANÇA \nPRECIONE 2 PARA CONTA CORRENTE\n>>"))

        if tipo_conta == 1:
            print(cliente_poupanca.consultar_historico_transacoes())
        elif tipo_conta ==2:
            print(cliente_corrente.consultar_historico_transacoes())

    # realiza simulações
    elif opcao == 5:
        
        data = input("Selecione a medida do tempo: \nAnos \nMeses \nDias \nHoras \nMinutos \nSegundo\n>> ")
        Quantidade = int(input("Quantidade de tempo investido: "))

        cliente_poupanca.verificar_rendimento(tempo=data, quantidade=Quantidade) 

    else:
        break
