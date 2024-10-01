# self é a forma da classe de se referir a ela mesma
# --init-- é o método construtor que criar o objeto da classe
class Conta:
    def __init__(self,numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

# Observe os parametros passados na criação do objeto
def main():
    c1 = Conta(numero=1, cpf=1, nomeTitular="João", saldo= 1000) # Objeto c1 sendo instânciado pela classe Conta
    print(f"Nome: {c1.nomeTitular}")
    print(f"CPF: {c1.cpf}")
    print(f"Número: {c1.numero}")
    print(f"Saldo: {c1.saldo}")

"""Quando um script python é executado, a variável reservada
Name referente a ele tem valor igual a "__main__".
Nesse caso, a condição do IF a seguir terá TRUE.
Então o que está no corpo do IF será executado. No caso,
é um chamado ao método main do script"""

if __name__ == "__main__":
    main()