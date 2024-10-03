# Permite a criação de tipos de exceções para diferenciar os erros gerados
# pelas bibliotecas da linguagem daqueles gerados pelas aplicações

class ExcecaoCustomizada(Exception): # Define a exceção costumizada
    pass

def checa_valor(valor): # definido um método que se for chamado, criará uma excessão
    if valor < 0 :
        raise ExcecaoCustomizada("Valor não pode ser negativo!")
    
def divide(a,b):
    return a / b