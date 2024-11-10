# Bem-Vindos ao Repositório de estudos de Lógica de Programação

Repositório criado para apoio nos estudos do Python, o qual abordará inicialmente uma introdução à Lógica de Programação Python, bem como conceitos especifícos do Python.

## Introdução à Lógica de Programação com Python

A lógica de programação é a base para desenvolver soluções computacionais. Envolve um conjunto de passos e regras para resolver problemas de forma sistemática, organizando o raciocínio para escrever programas que funcionem corretamente. Python é uma linguagem popular para aprender lógica de programação devido à sua simplicidade e legibilidade.

### Conceitos básicos de lógica de programação

1. O que é Lógica de Programação?

Lógica de programação é a prática de organizar um conjunto de instruções para alcançar um objetivo específico. Esse processo envolve:

- Identificação do problema.
- Divisão do problema em partes menores.
- Definição de uma sequência de passos (algoritmo) para resolver cada parte.

2. Algoritmos

Um algoritmo é uma sequência de instruções que resolve um problema. Um bom algoritmo é:

- Preciso: Define claramente cada etapa.
- Eficiente: Minimiza recursos e tempo.
- Compreensível: Fácil de entender e modificar.

**Exemplo de Algoritmo Simples**

Para encontrar o maior número entre dois valores:

- Compare os dois números.
- Se o primeiro for maior, ele é o resultado. 
- Caso contrário, o segundo é o resultado.

3. Lógica de Programação com Python

A lógica de programação é implementada em uma linguagem de programação. Python é muito usado para isso devido à sua sintaxe simples e intuitiva.

4. Conceitos Básicos em Python

**Variáveis**

Uma variável é um local onde armazenamos dados que serão usados em um programa.

Exemplo:

```
nome = "Alice"
idade = 25
```

**Tipos de Dados**

Python possui diferentes tipos de dados, como:

- Inteiros (int): números inteiros.
- Ponto flutuante (float): números com casas decimais.
- String (str): textos.

```
numero_inteiro = 10       # int
numero_decimal = 10.5     # float
texto = "Olá, mundo!"     # str
```

**Operadores**

Operadores são símbolos que realizam operações aritméticas, comparações e lógicas.

- Aritméticos: +, -, *, /, //, %, **
- Comparação: ==, !=, >, <, >=, <=
- Lógicos: and, or, not

```
a = 5
b = 3
print(a + b)  # Soma
print(a > b)  # Comparação
print(a > 2 and b < 5)  # Lógica
```

**Estruturas Condicionais**

Usamos estruturas condicionais para tomar decisões.

```
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

**Estruturas de Repetição**

As estruturas de repetição executam um bloco de código várias vezes, útil para percorrer listas ou repetir tarefas.

For: usado para iterar sobre uma sequência.

```
for i in range(5):
    print("Contagem:", i)
```

While: repete enquanto uma condição é verdadeira.

```
contador = 0
while contador < 5:
    print("Contagem:", contador)
    contador += 1
```