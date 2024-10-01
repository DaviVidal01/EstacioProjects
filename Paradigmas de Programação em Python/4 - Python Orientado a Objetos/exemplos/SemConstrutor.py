"""Classe sem método construtor
python não obrigada a existência do construtor
ele somente é necessário se o objeto a ser instanciado necessitar
de alguma ação como a inicialização e/ou atribuição de valores """

class A():
    def f(self):
        print("foo")

def main():
    obj_A = A() # Objeto sendo instanciado
    obj_A.f()

if __name__ == "__main__":
    main()