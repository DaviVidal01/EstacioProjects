# Criar uma classe pessoa que recebe parâmetro para o construtor
# a classe pessoa deve ter: nome e idade
# A classe pessoa deve ter um método de classe para receber o ano de nascimento
# e o nome da pessoa e calcular sua idade e um método estático
# que informe se a pessoa é maior ou menor de idade
from datetime import datetime

class Pessoa():
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    # Um metodo de classe para criar
    # um objeto pessoa a partir do ano de nascimento

    @classmethod
    def apartiranonasc(cls,nome,ano):
        return cls(nome, date.today().year - ano)
    # metodo estático para verificar se é maior de idade

    @staticmethod
    def ehmaior(idade):
        return idade >= 18
pessoa1 = pessoa("Ventury", 62)
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa.ehmaior(pessoa1.idade))
pessoa2 = pessoa.apartiranonasc('LUG',2013)
print(pessoa2.nome)
print(pessoa2.idade)
print(pessoa.ehmaior(pessoa2.idade))
    