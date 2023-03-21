print("Calculadora")

# solicita dois números do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# exibe as opções de operação
print("Selecione a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# solicita a escolha da operação ao usuário
escolha = int(input("Digite sua escolha (1/2/3/4): "))

# executa a operação escolhida e exibe o resultado
if escolha == 1:
    resultado = num1 + num2
    print(num1, "+", num2, "=", resultado)
elif escolha == 2:
    resultado = num1 - num2
    print(num1, "-", num2, "=", resultado)
elif escolha == 3:
    resultado = num1 * num2
    print(num1, "*", num2, "=", resultado)
elif escolha == 4:
    resultado = num1 / num2
    print(num1, "/", num2, "=", resultado)
else:
    print("Escolha inválida.")
