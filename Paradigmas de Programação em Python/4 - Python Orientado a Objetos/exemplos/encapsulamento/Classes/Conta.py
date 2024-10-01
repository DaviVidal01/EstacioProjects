class Conta:

    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo
        
        def sacar(self,valor):
            if self.saldo < valor:
                return False
            else:
                self.saldo -= valor
                self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
                return True