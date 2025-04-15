print("=== Mini Calculadora ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Escolha uma opção (1/2/3/4): ")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if opcao == '1':
    resultado = n1 + n2
    print(f"A soma entre {n1} e {n2} é {resultado}")
elif opcao == '2':
    resultado = n1 - n2
    print(f"A subtração entre {n1} e {n2} é {resultado}")
elif opcao == '3':
    resultado = n1 * n2
    print(f"A multiplicação entre {n1} e {n2} é {resultado}")
elif opcao == '4':
    if n2 != 0:
        resultado = n1 / n2
        print(f"A divisão entre {n1} e {n2} é {resultado}")
    else:
        print("Erro: não é possível dividir por zero.")
else:
    print("Opção inválida. Tente novamente.")
