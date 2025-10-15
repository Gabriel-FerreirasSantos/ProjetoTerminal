#função para dizer que o arquivo ja existe
def arquivo_ja_existe():
    print("O arquivo ja existe!")
    while True:
        print("Caso queira voltar pro menu digite [1]")
        print("Caso queira tentar novamente digite [2]")
        voltar_universal = input("Reposta :").strip()
        if voltar_universal.isdigit():
            voltar_universal = int(voltar_universal)
            if voltar_universal == 1:
                return False 
            elif voltar_universal == 2:
                return True
            else:
                print("Você não digitou um número da lista.")
        else:
            print(f"Você não digitou corretamente, não existe {voltar_universal}.")
            print("Digite corretamente.")