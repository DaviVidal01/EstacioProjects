from Classes.Conta import Conta
import datetime

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo, limite):
        # chama o construtor e inicializa os atributos herdados
        super().__init__(clientes, numero, saldo)
        # atributo limite exclusivo da ContaEspecial
        self.limite = limite

    # polimorfismo
    
    def sacar(self,valor):
        if (self.saldo + self.limite) < valor:
            print(f"Não existe saldo suficiente conta numero {self.numero}")
            return False
        else:
            self.saldo -= valor
            if (self.saldo < 0):
                self.limite += self.saldo
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True

    def depositar(self,valor):
        pass