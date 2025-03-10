from menu import Entrada
from cadastro import Cadastro
from rodando import Interno

def main():
    menu = Entrada()
    cadastro = Cadastro()
    programa = Interno(cadastro)
    continuar_programa = True

    while continuar_programa:
        print("\n\n\nBem-vindo ao Sistema! Escolha uma das opções abaixo:\n")
        menu.opcoes_inicio()
        if menu.escolha == '3':
            menu.clear_terminal()
            menu.exit_confirm()
            continuar_programa = False
        elif menu.escolha == '2':
            while True:
                menu.clear_terminal()
                print('Você escolheu Acessar um Perfil!')
                nome = input("Para voltar ao menu inicial digite 'X'\n\nDigite seu nome completo: ")
                if nome.strip().upper() == 'X':
                    print("Voltando ao menu inicial...\n\n\n")
                    break
                nome = cadastro.valida_nome(nome)
                if not cadastro.verifica_arquivo(nome, "nomes.txt"):
                    print(f"Usuário '{nome}' não encontrado. Tente novamente ou volte ao menu inicial!")
                    continue
                chave_acesso = input("Digite sua matrícula gerada ao se cadastrar: ")
                if cadastro.valida_acesso(nome, chave_acesso):

                    while True:
                        print(f"\nSeja bem-vindo ao programa {nome}\n")
                        menu.opcoes_programa()

                        if menu.escolha == "1":
                            menu.clear_terminal()
                            programa.new_info(nome)

                        elif menu.escolha == "2":
                            menu.clear_terminal()
                            programa.vist_profiles()
                            
                        elif menu.escolha == "3":
                            menu.clear_terminal()
                            programa.edit_exclude_arq(nome)

                        elif menu.escolha == "4": 
                            programa.imprime_relatorio(nome)

                        elif menu.escolha == "X":
                            menu.clear_terminal()
                            print("Voltando ao menu inicial...\n\n\n")
                            break

                        else:
                            print("Opção inválida! Tente novamente.")
                else:
                    print("Matrícula inválida, por favor tente novamente!")
        else:
            menu.clear_terminal()
            print('Você escolheu Cadastrar um novo usuário!')
            cadastro.cad_user()
    print("Programa encerrado! Até logo!")    

if __name__ == "__main__":
    main()
