frase = input("Digite uma frase: ")
palavras = frase.split()
frequencia = {}

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print("Frequência das palavras:")
for palavra, contagem in frequencia.items():
    print(f"{palavra}: {contagem}")