
#função para saber se é um digito ou não
def digitoOuNao():
    while True:
        escolha_universal = input("Qual você deseja? :").strip()
        if escolha_universal.isdigit():
            escolha_universal = int(escolha_universal)
            return int(escolha_universal)
        else:
            print("Você não digitou um número da lista")
            print("Digite um número válido")