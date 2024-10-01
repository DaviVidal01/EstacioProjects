import datetime

class Poupanca:
    def __init__(self,taxa_remuneracao):
        self.taxa_remuneracaoMes = taxa_remuneracao
        self.data_abertura = datetime.datetime.today()

    def remuneraConta(self): # Aplica a remuneração da conta
        self.saldo += self.saldo * self.taxa_remuneracaoMes