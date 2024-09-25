# CALCULO: quantos números pares existem de 0 a n 

# def conta_numeros_pares(n):
#  p = 0
#  for num in range(n+1):
#    if num%2 == 0:
#      p += 1
#  return p

# CALCULO RECURSIVO: quantos números pares existem de 0 a n

def conta_numeros_pares(n):
  if n == 0: return 1 # 0 é par
  elif n%2 == 0: return 1 + conta_numeros(n-1)
  else: return conta_numeros(n-1)