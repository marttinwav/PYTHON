print("Exemplo de captura de execções")
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        resultado = 10 / numero
        print(f"Resultado da divisão: {resultado}")
    except ValueError as e:
        print(f"Erro: {e}. Por favor, digite um número inteiro válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
