def calculadora():
    print("Calculadora com Adição, Subtração, Multiplicação e Divisão")
    
    while True:
        try:
            # Aqui vão ser a quantidade de numeros possiveis do usuario.
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            # Dado de entrada
            op = input("Digite a operação desejada (+, -, *, /): ")
            
            # Cálculos (com indentação correta)
            if op == '+':
                print(f"Resultado: {num1 + num2}")
            elif op == '-':
                print(f"Resultado: {num1 - num2}")
            elif op == '*':
                print(f"Resultado: {num1 * num2}")
            elif op == '/':
                if num2 == 0:
                    print("Erro: Não pode dividir por zero!")
                    continue
                print(f"Resultado: {num1 / num2}")
            else:
                print("Erro: Operação inválida! Use +, -, * ou /")
                continue
            
            break 
            
        except ValueError:
            print("Erro: Digite números válidos!")

calculadora()