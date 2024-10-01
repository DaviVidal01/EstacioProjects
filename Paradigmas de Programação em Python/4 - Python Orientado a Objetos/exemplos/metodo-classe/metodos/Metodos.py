# Método privado
# São indicados por um _ ou dois underscores __ no inóicio do nome

class MinhaClasse:
    def __init__(self):
        self._atributo_privado = 42
    
    def _metodo_privado1(self):
        print("Este é um método privado 1.")
    
    def metodo_publico1(self):
        print("Este é um método público 1.")
        self._metodo_privado1()

    def __metodo_privado2(self):
        print("Este é um método fortemente privado 2.")
    
    def metodo_publico2(self):
        print("Este é um método público 2.")
        self.__metodo_privado2()

obj = MinhaClasse()
obj.metodo_publico1() # Chama o método público1 que por sua vez chama um método privado
# Saída:
# Este é um método público1.
# Este é um método privado1.

# Embora não seja recomendado, você ainda pode chamar diretamente o método privado
obj._metodo_privado1() # Funciona embora não seja recomendado

obj.metodo_publico2() 
# Saída:
# Este é um método público2.
# Este é um método fortemente privado.abs

# Acessar diretamente o método fortemente privado não funciona:
# Para acessar, você teria que usar o nome "embaralhado".
obj._MinhaClasse__metodo_privado2() #Funciona, mas não é recomendado
# Saída:
# Este é um método fortemente privado2.