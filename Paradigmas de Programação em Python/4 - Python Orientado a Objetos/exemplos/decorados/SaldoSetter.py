from Classes.Contadec import Contadec

def main():
    conta = Contadec(1)
    conta.saldo = 1000 # usando o @saldo.setter
    print(f"saldo da conta = {conta.saldo}") # usando o @property

if __name__ == "__main__":
    main()