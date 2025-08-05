def calculadora():
    print("Calculadora Simples")
    print("Operacoes disponiveis:")
    print("1 - Adicao")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")

    operacao = input("Escolha a operacao (1/2/3/4): ")

    if operacao in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operacao == '1':
                resultado = num1 + num2
                print(f"{num1} + {num2} = {resultado}")
            elif operacao == '2':
                resultado = num1 - num2
                print(f"{num1} - {num2} = {resultado}")
            elif operacao == '3':
                resultado = num1 * num2
                print(f"{num1} * {num2} = {resultado}")
            elif operacao == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"{num1} / {num2} = {resultado}")
                else:
                    print("Erro: Divisão por zero.")
        except ValueError:
            print("Erro: Por favor, digite números válidos.")
    else:
        print("Operação inválida.")
        
calculadora()