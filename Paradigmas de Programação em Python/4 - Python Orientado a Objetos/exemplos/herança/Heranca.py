# testando herança
from Classes.Cliente import Cliente
from Classes.Conta import Conta
from Classes.ContaEspecial import ContaEspecial

cliente1 = Cliente("123", "Joao", "Rua X")
cliente2 = Cliente("456", "Maria", "Rua W")
cliente3 = Cliente("789", "Joana", "Rua H")

# As três contas foram iniciadas, as contas comuns com 2000 de saldo
conta1 = Conta(cliente1, 1, 2000)
conta2 = Conta(cliente2, 2, 2000)
conta3 = ContaEspecial(cliente3, 3, 1000, 2000)

# impresso o saldo das contas
print(f"Cliente: {cliente1.cpf} da conta comum {conta1.numero} possui saldo {conta1.saldo}")
print(f"Cliente: {cliente2.cpf} da conta comum {conta2.numero} possui saldo {conta2.saldo}")
print(f"Cliente: {cliente3.cpf} da conta especial {conta3.numero} possui saldo {conta3.saldo} com limite {conta3.limite}")

# Depositou 400 e tentou sacar 300 da conta comum que não terá saldo
conta2.depositar(500)
#Mensagem indicando saldo após depósito
print(f"Cliente: {cliente2.cpf} da conta comum {conta2.numero} possui saldo {conta2.saldo}")

conta2.sacar(3000)
# Mensagem indicando que não foi possível sacar o saldo
print(f"Cliente: {cliente2.cpf} da conta comum {conta2.numero} possui saldo {conta2.saldo}")

# depositou 100 e tentou sacar 200 da conta especial que tem limite
conta3.depositar(100)
# mensagem indicando o saldo após o depósito
print(f"Cliente: {cliente3.cpf} da conta especial {conta3.numero} possui saldo {conta3.saldo} com limite {conta3.limite}")

conta3.sacar(2000)
# mensagem indicando que foi possivel sacar o saldo negativo
print(f"Cliente: {cliente3.cpf} da conta especial {conta3.numero} possui saldo {conta3.saldo} com limite {conta3.limite}")

# tentativa de saque acima do limite
conta3.sacar(2000)
print(f"Cliente: {cliente3.cpf} da conta especial {conta3.numero} possui saldo {conta3.saldo} com limite {conta3.limite}")