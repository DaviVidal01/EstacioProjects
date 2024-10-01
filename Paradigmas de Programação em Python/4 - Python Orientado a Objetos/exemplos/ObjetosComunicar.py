class Conta:
    def __init__(self,numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor
    
    def sacar(self,valor):
        if self.saldo < valor: # Verifica se tem saldo para sacar.
            return False
        else:
            self.saldo -= valor
            return True
    
    def transfereValor(self,contaDestino, valor):
        if self.saldo < valor:
            return("Não existe saldo suficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return("Transferencia Realizada")

    def gerar_extrato(self):
        print(f"numero: {self.numero} \n cpf: {self.cpf} \n saldo: {self.saldo}")

def main():
    c1 = Conta(numero=1, cpf=123, nomeTitular="João", saldo=1000)
    c2 = Conta(numero=2, cpf=456, nomeTitular="Maria", saldo=500)

    print("Saldo antes da transferência")
    print(f"Saldo da conta 1: R${c1.saldo}")
    print(f"Saldo da conta 2: R${c2.saldo}")

    c1.transfereValor(c2,300)
    print("Saldo após a transferência")
    print(f"Saldo da conta 1: R${c1.saldo}")
    print(f"Saldo da conta 2: R${c2.saldo}")

if __name__ == "__main__":
    main()