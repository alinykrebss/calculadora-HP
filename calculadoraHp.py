
print("TABELA DE VALORES")
print("1 equivale a soma")
print("2 equivale a subtração")
print("3 equivale a multiplicação")
print("4 equivale a divisão\n")

print("Digite 'x' para sair.\n")

resultado = 0

while True:
    operacao = input("Escolha uma operação (1, 2, 3, 4): ")
    
    if operacao.lower() == 'x':
        print(f"Resultado final: {resultado}")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == '1':
        resultado += num1 + num2
    elif operacao == '2':
        resultado += num1 - num2
    elif operacao == '3':
        resultado += num1 * num2
    elif operacao == '4':
        resultado += num1 / num2
    else :
        print("por favor coloque um numero válido, como na lista de valores")

    print(f"Resultado guardado: {resultado}\n")

print("Calculadora encerrada!")


