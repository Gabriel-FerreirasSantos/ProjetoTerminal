from pathlib import Path

#utilidades gerais e genericas
from utils.limpar_tela import limpar_tela
from utils.digitoOunao import digitoOuNao
from utils.menu import menu

#funções da case 1
from utils.caracter_invalido import resposta_caracter_invalido
from create_file.criar_arquivo_novamente import criar_arquivo_novamente
from create_file.colocar_txt_no_final_arquivo import convertendo_arquivo_txt
from create_file.verificar_se_arquivo_existe import arquivo_ja_existe
from create_file.criar_arquivo import criar_arquivo

#Uma variavel apenas para verificar o menu principal, caso o usuario quiser sair em breve
verificador_menu_principal = True

while verificador_menu_principal == True:
    menu_case1 = True
    menu_renomear_arquivo = True
    #apenas menu estético
    limpar_tela()
    menu()
    
    #variavel numero da escolha recebe o return da função se é um digito ou não
    numero_da_escolha_menu = digitoOuNao()

    #Um switch improvissado 
    match numero_da_escolha_menu:

        #Criar arquivo
        case 1:
            limpar_tela()
            #Main
            while menu_case1 == True:
                nome_arquivo = input("Digite o nome do arquivo :")
                
                #Colocar .txt no final
                nome_arquivo = convertendo_arquivo_txt(nome_arquivo)

                #caracteres
                caracteres_invalidos = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']

                #Verifica se tem caractere invalido para não dar um erro
                if any(c in nome_arquivo for c in caracteres_invalidos):
                    limpar_tela()
                    resposta_caracter_invalido()
                else:
                    #Criar o arquivo
                    try:
                        nome_arquivo = criar_arquivo(nome_arquivo)
                        limpar_tela()
                        print("Arquivo criado com sucesso!")
                        deseja_voltar = criar_arquivo_novamente()
                        limpar_tela()
                        if not deseja_voltar:
                            menu_case1 = False
                                

                    except FileExistsError:
                        limpar_tela()
                        deseja_voltar = arquivo_ja_existe()
                        limpar_tela()
                        if deseja_voltar == False:
                            menu_case1 = False

                    #except Exception as e:
                        #print(f"Erro ao criar o arquivo: {e}")
                        #deseja_voltar = refazer_case1()
                       #if not deseja_voltar:
                           # menu_case1 = False
                            
        case 2:
            limpar_tela()
            
            while menu_renomear_arquivo == True:

                #nome do arquivo
               
                def convertendo_arquivo_txt(nome):
                    nome = Path(nome)
                    return nome.with_suffix('.txt')

                nome_arquivo = input("Digite o nome do arquivo que deseja renomear: ")
                nome_arquivo = convertendo_arquivo_txt(nome_arquivo)

                novo_nome_arquivo = input("Digite o novo nome do arquivo: ")
                novo_nome_arquivo = Path(novo_nome_arquivo).with_suffix('.txt')  # Aqui salva o novo nome com .txt

                if nome_arquivo.exists():
                    nome_arquivo.rename(novo_nome_arquivo)
                    print("Arquivo renomeado com sucesso!")
                else:
                    print("O arquivo que você digitou não existe.")


        case 4:
            limpar_tela()
            verificador_menu_principal = False

        case _:
            print(22*"-")
            print("Parece que você não digitou um numero da lista!")
            print(f"Erro: Número {numero_da_escolha_menu} inexistente")
            input("Pressione qualquer tecla para voltar...")
