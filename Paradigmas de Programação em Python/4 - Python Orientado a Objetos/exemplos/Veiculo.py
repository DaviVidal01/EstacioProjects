from abc import ABC, abstractmethod

# Classe abstrata veículo
class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def ligar(self):
        pass

# SubClasse carro
class Carro(Veiculo):
    def mover(self):
        return "O carro está se movendo"
    
    def ligar(self):
        return "O carro está ligado."

# Subclasse bicicleta

class Bicicleta(Veiculo):
    def mover(self):
        return "A bicicleta está se movendo."
    
    def ligar(self):
        return "Não é possível ligar uma bicicleta"
    
carro = Carro()
bicicleta = Bicicleta()

print(carro.mover())
print(bicicleta.mover())

print(carro.ligar())
print(bicicleta.ligar())

