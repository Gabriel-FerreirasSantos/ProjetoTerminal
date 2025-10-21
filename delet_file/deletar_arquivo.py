from pathlib import Path

def deletar_arquivo(caminho_arquivo):
    caminho = Path(caminho_arquivo)
    try:
        if caminho.is_file():
            caminho.unlink()
            return True
        else:
            print("O caminho não é um arquivo ou não existe.")
            return False
    except Exception as e:
        print(f"Erro ao deletar: {e}")
        return False