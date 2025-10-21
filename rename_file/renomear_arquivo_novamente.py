#perguntar se o usuario deseja criar um novo arquivo
def renomear_arquivo_novamente():
    while True:
        renomear_novo_arquivo = input("Deseja renomear um novo arquivo? [S/N]:").upper().strip()
        if renomear_novo_arquivo in ("S", "SI", "SIM"):
            return True
        elif renomear_novo_arquivo in ("N", "NAO", "NÂO"):
            return False
        else:
            print("Entrada invalidá. Por favor, digite S ou N.")