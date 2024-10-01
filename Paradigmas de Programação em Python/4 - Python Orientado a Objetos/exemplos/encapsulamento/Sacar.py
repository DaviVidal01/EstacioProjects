def sacar(self,valor):
    if self.saldo < valor:
        return False
    else:
        self.saldo -= valor
        self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
        return True