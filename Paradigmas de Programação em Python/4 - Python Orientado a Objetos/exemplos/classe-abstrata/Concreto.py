# classe abstrata e método abstrato
# classe que não pode ser instanciada
from abc import ABC, abstractmethod
# abc (Abstract Base Classes). super classe de uma classe abstrata
class ContaCliente(ABC):
    def __init__(self,numero, IOF, IR, valorinvestido,taxarendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorinvestido = valorinvestido
        self.taxarendimento = taxarendimento
    # decorator @abstractmethod para indicar que o método calculo_rendimento
    @abstractmethod
    def CalculoRendimento(self):
        pass

class ContaReal(ContaCliente):
    def __init__(self,numero, IOF,IR,valorinvestido, taxarendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorinvestido = valorinvestido
        self.taxarendimento = taxarendimento

    def CalculoRendimento(self):
        pass

cc1 = ContaReal(1,0.1,0.25,10.1, 10)
print(cc1)
print(cc1.numero)
print(cc1.valorinvestido)