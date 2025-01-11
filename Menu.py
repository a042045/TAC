def menu():
    while True:
        print("\nMenu Principal")
        print("1. Agachamentos")
        print("2. Flexões")
        print("3. Sair")

        try:
            escolha = int(input("Escolha uma opção (1, 2 ou 3): "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if escolha == 1:
            agachamentos()
        elif escolha == 2:
            flexoes()
        elif escolha == 3:
            print("A sair... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def agachamentos():
    import Agachamentos

def flexoes():
    import Flexões

# Executa o menu
menu()