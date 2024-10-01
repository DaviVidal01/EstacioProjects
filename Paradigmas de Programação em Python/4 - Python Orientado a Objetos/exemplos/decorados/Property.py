# Utilizando métodos decorados

class Conta:
    def __init__(self,numero):
        self.numero = numero
        self._saldo = 0 # note o uso de somente um _

    # Utilizando o decorator @property, podemos proteger os atributos
    # e acessá-os somente por meio de métodos "decorados"
    @property #definindo método decorado
    def saldo(self):
        return self._saldo
    
    # O decorator @setter força todas as alterações de valor dos
    # atributos privados a passar por esses métodos
    @saldo.setter # definindo método setter
    def saldo(self,saldo):
        if saldo < 0:
            print("saldo inválido")
        else:
            self._saldo = saldo