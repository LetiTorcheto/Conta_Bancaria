#ContaPoupanca taxaDeRendimento
#taxa de rendimento ao ano 

from Conta import  Conta

class Conta_Poupanca(Conta):
    def __init__(self, IdConta, Saldo) -> None:
        super().__init__(IdConta, Saldo)
        # taxa de rendimento pre estabelecida
        self.Taxa_Rendimento = 12

    # Get
    def Get_IdConta(self):
        return self.IdConta

    def Get_Saldo(self):
        return self.Saldo
    
    # Set
    
    def Set_IdConta(self, Id):
        self.IdConta = Id
    def Set_IdConta(self, saldo):
        self.Saldo = saldo

    def sacar(self, valor):
        try:
            if int != type(valor) != float or valor <= 0:
                raise ValueError("Valor Inválido.")
            if self.Saldo >= valor:
                self.Saldo -= valor
                print(f"Saque realizado com sucesso!\nSaldo atual: R${self.Saldo:.2f}.")
                self.Transacoes.append({f"Saque realzado no valor de:R${valor}"})

            else:
                raise ValueError("Saldo insuficiente")

        except ValueError as error:
            print(error)

    def depositar(self, valor):
        try:
            if int != type(valor) != float or valor <= 0:
                raise ValueError("Valor Inválido.")
                
            else:
                self.Saldo += valor
                print(f"Depósito realizado com sucesso! \nSaldo atual: R${self.Saldo:.2f}.")
                self.Transacoes.append({f"Deposito realzado no valor de: R${valor}"})
        
        except ValueError as error:
            print(error)


    # Taxa definida pelos dias atuais
    def verificar_rendimento(self, tempo,  quantidade):
        try:
            if tempo.upper() == "Anos":
                rendimento = (self.Taxa_Rendimento * quantidade * self.Saldo) / 100
                print(f"Em {quantidade} anos, o saldo atual renderá um total de R${rendimento:.2f}")
            
            elif tempo.upper() == "MESES":
                rendimento = (self.Taxa_Rendimento * quantidade * self.Saldo) / 1200
                print(f"Em {quantidade} mêses, o saldo atual renderá um total de R${rendimento:.2f}")

            elif tempo.upper() == "SEMANAS":
                rendimento = (self.Taxa_Rendimento * quantidade * self.Saldo) / 5200
                print(f"Em {quantidade} semanas, o saldo atual renderá um total de R${rendimento:.2f}")        

            elif tempo.upper() == "DIAS":
                rendimento = (self.Taxa_Rendimento * quantidade * self.Saldo) / 36500
                print(f"Em {quantidade} dias, o saldo atual renderá um total de R${rendimento:.2f}") 

            elif tempo.upper() == "HORAS":
                rendimento = (self.Taxa_Rendimento * quantidade * self.Saldo) / 876000
                print(f"Em {quantidade} horas, o saldo atual renderá um total de R${rendimento:.2f}")  

            elif tempo.upper() == "MINUTOS":
                rendimento = (self.Taxa_Rendimento * quantidade * self.Saldo) / 52560000
                print(f"Em {quantidade} minutos, o saldo atual renderá um total de R${rendimento:.2f}")
            
            elif tempo.upper() == "SEGUNDOS":
                rendimento = (self.Taxa_Rendimento * quantidade * self.Saldo) / 3153600000
                print(f"Em {quantidade} segundos, o saldo atual renderá um total de R${rendimento:.2f}")
            
            else:
                ValueError("Não existe esta unidade de tempo")

        except ValueError as error:
            print(error)

    def consultar_historico_transacoes(self):
        try:
            if len(self.Transacoes) != 0 :
                self.Transacoes.insert(0,'Histórico de Transações:')
                print(self.Transacoes)
                print(f"O saldo atual agora é de  R${self.Saldo:.2f}")
            else:
                print("Ainda não fo realizada nenhuma operação!")

        except ValueError as error:
            print(error)
        
