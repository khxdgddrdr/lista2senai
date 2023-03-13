numero = int(input("Digite um número inteiro: "))

for i in range(1, 101):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)