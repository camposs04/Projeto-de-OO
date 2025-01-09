import os

class Entrada:
    def __init__(self):
        self.escolha = None


    def clear_terminal(self):
        if os.name == 'nt':  
            os.system('cls') #Windows

        else:  
            os.system('clear') # macOS e Linux
        

    def valida_respi(self, resp, intervalo):
        while resp not in intervalo:
            resp = input("Resposta inválida! digite entre as opções dadas: ")
        return resp


    #Exibir o Menu inicial e obtém a resposta
    def opcoes_inicio(self):
        intervalo = ['1','2','3']
        resp = input(" [1] Cadastrar novo usuario.\n [2] Acessar Perfil.\n [3] Encerrar o programa.\n\n Digite sua escolha: ").strip()
        self.escolha = self.valida_respi(resp,intervalo)


    def exit_confirm(self):
        opcao = input("Se deseja realmente encerrar o programa digite 'ENCERRAR'\n Qualquer coisa diferente disso o redirecionará para o início: ").strip().upper()
        if opcao == 'ENCERRAR':
            print('Programa Encerrado com sucesso!')
            exit()

        else:
            self.opcoes_inicio()


    def opcoes_programa(self):
        intervalo = ['1','2','3','4','X']
        entrada = input("  [1]Cadastrar Novas Informações.\n  [2]Pesquisar Perfis.\n  [3]Editar ou Excluir informações cadastradas.\n  [4]Gerar Meu relatório \n  [X]Sair do meu perfil \n\n Digite sua escolha: ").strip()
        self.escolha = self.valida_respi(entrada,intervalo)