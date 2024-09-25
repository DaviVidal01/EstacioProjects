# Função de exemplo: dobrar números
def dobrar(n):
    return n * 2

# Lista de números
numeros = [1,2,3,4,5]

# Aplicando a função dobrar usando map
numeros_dobrados = list(map(dobrar,numeros))

# Imprimindo os resultados
print("Números originais:", numeros)
print("Números dobrados:", numeros_dobrados)