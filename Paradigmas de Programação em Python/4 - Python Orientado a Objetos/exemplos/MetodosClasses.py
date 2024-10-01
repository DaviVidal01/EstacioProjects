# Métodos de Classes
# definem as ações que o objeto pode realizar
class Conta:
    def __init__(self,numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
    
    def depositar(self,valor):
        self.saldo += valor
    
    def sacar(self,valor):
        self.saldo -= valor
    
    def gerar_extrato(self):
        print(f"numero: {self.numero} \n cpf: {self.cpf} \n saldo: {self.saldo}")

def main():
    c1 = Conta(numero=1, cpf=1, nomeTitular="João", saldo=0)
    c1.depositar(300) # chamando o método depositar para c1
    c1.gerar_extrato() # chamando o método gerar extrato para c1
    c1.sacar(100) # chamando o método sacar para c1
    c1.gerar_extrato() # chamando o método gerar extrato para c1

if __name__ == "__main__":
    main()