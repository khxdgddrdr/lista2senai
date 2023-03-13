num = int(input("Digite um número inteiro: "))
fatores_primos = []

# Encontrando os fatores primos
divisor = 2
while num > 1:
    while num % divisor == 0:
        fatores_primos.append(divisor)
        num = num / divisor
    divisor += 1

# Exibindo os fatores primos encontrados
print("Fatores primos:", fatores_primos)
