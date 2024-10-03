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
    def calculo_rendimento(self):
        pass
#cc1 = ContaCliente(1,0.1,0.25,0.1)
