"""Elabore um programa em Python para calcular média de quatro números e exiba o resultado para o usuário.
Use as seguintes notas como entrada de dados do seu programa: 8, 9, 10 e 5."""
def media(n1,n2,n3,n4):
    media = (n1 + n2 + n3 + n4)/4
    return media
print("A média é:", media(8,9,10,5))