class Circulo:
    totalCirculos = 0 #atributo da classe fora do init

    def __init__(self,pontox,pontoy,raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        Circulo.totalCirculos +=1
