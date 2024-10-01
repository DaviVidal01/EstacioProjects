import datetime
from Classes.Extrato import Extrato

class Conta:
    def __init__(self,clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()
    
    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today()])
    
    def sacar(self,valor):
        if (self.saldo) < valor:
            print(f"Não existe saldo suficiente conta número: {self.numero}")
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True

    def transfereValor(self, contaDestino, valor):
      if self.saldo < valor:
            return("Não existe saldo suficiente")
      else:
            contaDestino.depositar(valor)
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
            self.saldo -= valor
            return("Transferencia Realizada")
    
    def gerar_saldo(self):
        print(f"Conta: {self.numero}")
        print(f"Saldo: R${self.saldo:10.2f}")