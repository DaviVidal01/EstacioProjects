import Sacar

class Conta:
    def __init__(self,numero,saldo):
        self.__numero = numero # Atributo privado
        self.saldo = saldo # Atributo privado

def main():
    conta = Conta(1, 1000)
    saldo = conta.saldo
    print(saldo)

if __name__ == "__main__":
    main()