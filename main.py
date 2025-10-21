from pathlib import Path

#utilidades gerais e genericas
from utils.limpar_tela import limpar_tela
from utils.digitoOunao import digitoOuNao
from utils.menu import menu
from utils.voltar_universal import voltar_universal

#funções da case 1
from utils.caracter_invalido import resposta_caracter_invalido
from create_file.criar_arquivo_novamente import criar_arquivo_novamente
from create_file.colocar_txt_no_final_arquivo import convertendo_arquivo_txt
from create_file.verificar_se_arquivo_existe import arquivo_ja_existe
from create_file.criar_arquivo import criar_arquivo

#funções da case 2
from rename_file.convertendo_arquivo_para_txt_rename import convertendo_arquivo_txt_rename
from rename_file.renomear_arquivo_novamente import renomear_arquivo_novamente

#funções da case3
from delet_file.deletar_arquivo import deletar_arquivo



#Uma variavel apenas para verificar o menu principal, caso o usuario quiser sair em breve
verificador_menu_principal = True

#programa
while verificador_menu_principal == True:
    #variaveis do subsmenus
    menu_criar_arquivo = True
    menu_renomear_arquivo = True
    menu_deletar_arquivo = True
    
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
            while menu_criar_arquivo == True:
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
                            menu_criar_arquivo = False
                                

                    except FileExistsError:
                        limpar_tela()
                        deseja_voltar = arquivo_ja_existe()
                        limpar_tela()
                        if deseja_voltar == False:
                            menu_criar_arquivo = False

                    #except Exception as e:
                        #print(f"Erro ao criar o arquivo: {e}")
                        #deseja_voltar = refazer_case1()
                        #if not deseja_voltar:
                            #menu_case1 = False
                            
        case 2:
            limpar_tela()
            
            #main
            while menu_renomear_arquivo == True:

                #limpar tela
                limpar_tela()
                
                #nome do arquivo
                nome_arquivo = input("Digite o nome do arquivo que deseja renomear: ")
                nome_arquivo = convertendo_arquivo_txt_rename(nome_arquivo) #converte para txt

                #verifica se o arquivo existe e se é arquivo
                if nome_arquivo.exists and nome_arquivo.is_file():

                    novo_nome_arquivo = input("Digite o novo nome do arquivo: ")
                        
                    #Lista com os caracteres invalidos
                    caracteres_invalidos = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']

                    #Verifica se tem caractere invalido para não dar um erro
                    if any(c in novo_nome_arquivo for c in caracteres_invalidos):
                        limpar_tela()
                        print(f"Erro: caracteres invalidos {novo_nome_arquivo}")
                        print("Deseja voltar para o menu principal digite [1]")
                        print("Deseja tentar renomear novamente digite [2]")
                        deseja_voltar = voltar_universal()
                        if deseja_voltar == True:
                            menu_renomear_arquivo = False
                        else:
                            pass

                    else:

                        try:
                            #convertendo o novo arquivo para txt
                            novo_nome_arquivo = convertendo_arquivo_txt_rename(novo_nome_arquivo)
                            nome_arquivo.rename(novo_nome_arquivo) #renomeando
                        except Exception as e:
                            print(f"Erro ao renomear: {e}")
                                
                            deseja_voltar = renomear_arquivo_novamente()

                        limpar_tela()
                        print("Arquivo renomeado com sucesso!")
                        deseja_voltar = renomear_arquivo_novamente()
                        if not deseja_voltar == True:
                            menu_renomear_arquivo = False
                else:
                    limpar_tela()
                    print(21*"=-=")
                    print(f"O arquivo que você digitou não existe ou não existe. '{nome_arquivo}'")
                    print(21*"=-=")
                    print("Deseja voltar para o menu principal digite [1]")
                    print("Deseja tentar renomear novamente digite [2]")
                    deseja_voltar = voltar_universal()
                    if deseja_voltar == True:
                        menu_renomear_arquivo = False
                    else:
                        pass

        case 3:
            
            while True:
                arquivo_que_quer_deletar = input("Qual o nome do arquivo que você deseja excluir? :")

                #colocando txt no final do arquivo
                arquivo_que_quer_deletar = convertendo_arquivo_txt(arquivo_que_quer_deletar)

                #transformando em path
                arquivo_que_quer_deletar = Path(arquivo_que_quer_deletar)

                #verificar se o arquivo path existe
                if arquivo_que_quer_deletar.exists():

                    deletar_arquivo(arquivo_que_quer_deletar)
                    print("Arquivo deletado com sucesso")
                    
                    break

                else:
                    print("Erro: o arquivo que voce digitou não existe")

        case 4:
            limpar_tela()
            verificador_menu_principal = False

        case _:
            print(22*"-")
            print("Parece que você não digitou um numero da lista!")
            print(f"Erro: Número {numero_da_escolha_menu} inexistente")
            input("Pressione qualquer tecla para voltar...")
