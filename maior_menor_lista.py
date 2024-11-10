# Encontrar o Maior e o Menor Número em uma Lista
numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))
maior = max(numeros)
menor = min(numeros)

print("Maior número:", maior)
print("Menor número:", menor)