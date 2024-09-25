"""O programa deve solicitar ao cliente a quantidade de cada produto adquirido e calcular o total da compra com base nos preços unitários dos itens.
Utilize os conceitos de atribuição, entrada e saída de dados para implementar o programa."""
preco_arroz = 10.00
preco_feijao = 8.50
preco_macarrao = 5.25

quantidade_arroz = int(input("Digite a quantidade de pacotes de arroz: "))
quantidade_feijao = int(input("Digite a quantidade de pacotes de feijão: "))
quantidade_macarrao = int(input("Digite a quantidade de pacotes de macarrão: "))

total_compra = (preco_arroz * quantidade_arroz) + (preco_feijao * quantidade_feijao) + (preco_macarrao * quantidade_macarrao)

print("O total da sua compra é: R$", total_compra)