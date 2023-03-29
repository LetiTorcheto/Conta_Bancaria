#Conta
#id_conta, saldo
#metodos depositar, sacar
#getters, setters dos atributos

from abc import ABC, abstractclassmethod

# A classe conta bancaria recebe atributos bases para as classes ContaCorrente e ContaPupanca
class Conta(ABC):
    def __init__(self, IdConta, Saldo) -> None:        
        self.IdConta = IdConta
        self.Saldo = Saldo
        self.Transacoes = []
    # Get
    @abstractclassmethod
    def Get_IdConta(self):
        pass
    
    @abstractclassmethod
    def Get_Saldo(self):
        pass
    
    # Set
    @abstractclassmethod
    def Set_IdConta(self, Id):
        pass

    @abstractclassmethod
    def Set_IdConta(self, saldo):
        pass

    # Metodo base para a realização do saque
    @abstractclassmethod
    def sacar(self, valor):
        pass

    # Metodo base para a realização de um deposito
    @abstractclassmethod
    def depositar(self, valor):
       pass

    # Metodo base para Consultar o saldo independente do tipo da conta
    def ConsultaSaldo(self):
        pass

    def consultar_historico_transacoes(self):
       pass
    


    
    

