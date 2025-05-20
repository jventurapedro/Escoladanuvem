def registrar_notas():
    print("Registro de Notas da Turma")
    print("Digite as notas (0 a 10) ou 'fim' para terminar:")
    
    notas = []
    
    while True:
        entrada = input("Nota: ")
        
        if entrada.lower() == 'fim':
            break
            
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número ou 'fim'.")
    
    if notas:
        media = sum(notas) / len(notas)
        print(f"\nMédia da turma: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi registrada.")

# Executar o programa
registrar_notas()