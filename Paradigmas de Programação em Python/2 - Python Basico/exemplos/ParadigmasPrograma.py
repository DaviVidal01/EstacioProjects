# Programação Procedural
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
print("Fatorial de 5 (procedural):", fatorial(5))

# Programação Orientada a Objetos
class Fatorial:
    def calcular(self,n):
        if n == 0:
            return 1
        else:
            return n * self.calcular(n-1)
f = Fatorial()
print("Fatorial de 5 (orientado a objetos):", f.calcular(5))