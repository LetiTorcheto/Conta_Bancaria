

from Conta import  Conta

#cartã de debito:
class Conta_Corrente(Conta):
    def __init__(self, Limite, IdConta, Saldo) -> None:
        super().__init__(IdConta, Saldo)
        self.limite_inicia = Limite
        self.Limite = Limite


    # O saque so é realzado quando ele for um numero maior que 0
    def sacar(self, valor):
        try:
            if int != type(valor) != float or valor <= 0:
                raise ValueError("Valor Inválido.")
            elif self.Limite + self.Saldo < valor:
                raise ValueError(f"O valor incerido excede o seu limite")
            else:
                self.Saldo =- valor
                self.Transacoes.append({f"Saque realzado no valor de: R${valor:.2f}"})
        except ValueError as error:
            print(error)
        
    # O deposto so é realzado quando ele for um numero maior que 0
    def depositar(self, valor):
        try:
            if int != type(valor) != float or valor <= 0:
                raise ValueError("Valor Invalido.")
            else:
                self.Saldo =+ valor
                self.Transacoes.append({f"Deposito realzado no valor de: R${valor:.2f}"})
        except ValueError as error:
            print(error)
    
  
    def Get_IdConta(self):
        return self.IdConta

    def Get_Saldo(self):
        return self.Saldo
    
    # Set
    
    def Set_IdConta(self, Id):
        self.IdConta = Id
    def Set_IdConta(self, saldo):
        self.Saldo = saldo

    def consultar_historico_transacoes(self):
        try:
            if len(self.Transacoes) != 0 :
                self.Transacoes.insert(0,'Histórico de Transações:')
                print(self.Transacoes)
                print(f"O saldo atual agora é de R${self.Saldo:.2f}")
            else:
                print("Ainda não fo realizada nenhuma operação!")

        except ValueError as error:
            print(error)
