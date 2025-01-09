class Interno:
    def __init__(self, cadastro):
        self.cadastro = cadastro
        

    #Adicionar informações ao currículo de uma pessoa
    def new_info(self,nome):

        arquivo_pessoal = f"{nome}.txt"
        info = input("Digite aqui as Habilidades de deseja cadastrar (o que for escrito será salvo em uma linha!): ")

        try:
            with open(arquivo_pessoal,'a') as arquivo:
                arquivo.write(f"{info}\n")
            print(f"'{info}' - FOI ADICIONADO COM SUCESSO!")

        except FileNotFoundError:
            with open(arquivo_pessoal,'w') as arquivo:
                arquivo.write(f"{info}\n")
        

    #Retornar os dados de um arquivo separadamente
    def list_info(self,arquivo_pessoal):
            
        try:    
            with open(arquivo_pessoal,'r') as arquivo:
                linhas = arquivo.readlines()
                return [linha.strip() for linha in linhas]
            
        except FileNotFoundError:
            print("Nada foi cadastrado ainda!")
            return []
                    

    #Procura por perfis de acordo com o nome desejado
    def vist_profiles(self):
        
        nome_desj = input("Qual o nome da pessoa que deseja visitar o perfil? ")
        nome_desj = self.cadastro.valida_nome(nome_desj)
    
        if self.cadastro.verifica_arquivo(nome_desj,'nomes.txt'):
            nome_arq = f'{nome_desj}.txt'
            informacoes = self.list_info(nome_arq)

            print(f"Perfil de {nome_desj}")
            for dados in informacoes:
                print(f"-{dados}")

        else:
            print(f"Nenhum usuário {nome_desj} foi encontrado :(")


    #Edição do arquivo
    def edit_exclude_arq(self, usuario):

        nome_arq = f"{usuario}.txt"

        informacoes = self.list_info(nome_arq)

        if not informacoes:
            print("Nenhuma informação foi cadastrada até o momento!")
            return
    
        print("Informações cadastradas:")
        for idx, info in enumerate(informacoes, start = 1):
            print(f"{idx}. {info}")

        escolha = int(input("Digite o número da informação que deseja editar/excluir: ").strip())

        while escolha < 0 or escolha >= len(informacoes):
            escolha = int(input("Opção inválida. Por favor digite novamente: ").strip())

        acao = input("Digite 'E' para editar ou 'X' para excluir (Qualquer outra informação o levará para o menu): ").upper()

        if acao == 'E':
            nova_info = input("Digite a nova informacao: ")
            nome_arq[escolha] = nova_info

        elif acao == 'X':
            nome_arq.pop(escolha)

        else:
            print("\nNada foi alterado!\n")

        with open(nome_arq,'w') as arquivo:
            for linha in informacoes:
                arquivo.write(f"{linha}\n")

        
    def imprime_relatorio(self,nome):
        arq = f"{nome}.txt"
        informacoes = self.list_info(arq)

        if informacoes:
            print(f"\n Relatório de {nome}\n")
            for dados in informacoes:
                print(dados)

        else:
            print("Nenhuma informação encontrada.")