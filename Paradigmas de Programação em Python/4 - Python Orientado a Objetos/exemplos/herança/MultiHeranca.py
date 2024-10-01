from Classes.Cliente import Cliente
from Classes.Conta import Conta
from Classes.Poupanca import Poupanca
from Classes.ContaRemuneradaPoupanca import ContaRemuneradaPoupanca

cliente1 = Cliente("123", "Joao", "Rua X")
cliente2 = Cliente("456", "Maria", "Rua W")

conta1 = Conta([cliente1, cliente2], 1, 2000)
contapoupanca1 = Poupanca(0.1)
contaremunerada1 = ContaRemuneradaPoupanca(0.1, [cliente1], 5, 1000)

contaremunerada1.remuneraConta()
contaremunerada1.gerar_saldo()