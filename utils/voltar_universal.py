
def voltar_universal():
     while True:
        voltar = input("Resposta:").upper().strip()
        if voltar == "1":
            return True
        elif voltar == "2":
            return False
        else:
            print("Entrada invalidá. Por favor, digite 1 ou 2.")