import os

def limpar_tela():
    # 'cls' para Windows, 'clear' para Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')