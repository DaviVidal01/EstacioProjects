# Atribuição de Valores a Variáveis
nome = "Alice"
idade = 30
# Entrada de dados do usuário
altura = float(input("Digite a sua altura em metros: "))
peso = float(input("Digite o seu peso em kg: "))
# Cálculo do IMC (Índice de Massa Corporal)
imc = peso / (altura**2)
# Saída de dados formatada
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura:.2f}m")
print(f"Peso: {peso:.1f}kg")
print(f"IMC: {imc:.2f}")
### Exemplo de Saída:
# Digite a sua altura em metros: 1.75
# Digite o seu peso em kg: 68
# Nome: Alice
# Idade: 30
# Altura: 1.75m
# Peso: 68.0kg
# IMC: 22.20