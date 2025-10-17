from pathlib import Path

def convertendo_arquivo_txt_rename(nome):
    nome = Path(nome)
    return nome.with_suffix('.txt')