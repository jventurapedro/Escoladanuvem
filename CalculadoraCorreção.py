def calculadora():
    #Solicitação dos mumeros a serem calculados
    try:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo número: "))

        #Solicitação da operação a ser realizada

        operacao = input("Digite a operação desejada (+, -, *, /): ")

        if operacao == ""+"":
            resultado = num1 + num2
        elif operacao == ""-"":
            resultado = num1 - num2
        elif operacao == ""*"":
            resultado = num1 * num2
        elif operacao == ""/"":
            if num2 == 0:
                print("ERRO: Divisão por zero não é permitida.")
            resultado = num1 / num2

        print("O resultado da operação é:", resultado)
        

    except ValueError: