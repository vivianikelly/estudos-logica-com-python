# Fibonacci até um Número Dado

def fibonacci(limite):
    a, b = 0, 1
    while a <= limite:
        print(a, end=" ")
        a, b = b, a + b

limite = int(input("Digite o limite da sequência de Fibonacci: "))
fibonacci(limite)