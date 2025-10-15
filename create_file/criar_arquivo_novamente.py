#perguntar se o usuario deseja criar um novo arquivo
def criar_arquivo_novamente():
    while True:
        criar_novo_arquivo = input("Deseja criar um novo arquivo? [S/N]:").upper().strip()
        if criar_novo_arquivo in ("S", "SI", "SIM"):
            return True
        elif criar_novo_arquivo in ("N", "NAO", "NÂO"):
            return False
        else:
            print("Entrada invalidá. Por favor, digite S ou N.")