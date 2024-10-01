from Classes.Conta import Conta
from Classes.Poupanca import Poupanca

class ContaRemuneradaPoupanca(Conta, Poupanca):
    def __init__(self, taxa_remuneracao, clientes, numero, saldo):
        # inicializar os atributos herdados da classe Conta
        Conta.__init__(self,clientes,numero,saldo)
        # inicializar os atributos herdados da classe Poupanca
        Poupanca.__init__(self,taxa_remuneracao)
    
    def remuneraConta(self):
        self.saldo += self.saldo * (self.taxaremuneracaoMes / 30)