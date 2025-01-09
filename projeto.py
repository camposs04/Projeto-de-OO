import os

class Cadastros:
    
    def __init__(self):
        self.usuarios = []


    def valida_nome(self, nome):
    #Valida se o nome contém apenas letras, tem espaços apropriados e possui pelo menos 6 caracteres.
        while (
            not nome.replace(" ", "").isalpha() # Permite apenas letras e espaços
            or len(nome) < 6  # Comprimento mínimo
            or " " not in nome  # Verifica se há pelo menos um espaço (nome e sobrenome)
        ):
            nome = input(
                "Nome inválido! Digite um nome completo (apenas letras, com pelo menos 6 caracteres e um espaço): "
            ).strip()  # Remove espaços extras no início ou no final
        return nome

    
    
    #Gera uma matrícula única por usuário
    def gera_matricula(self):
        try:
            with open('matriculas.txt', 'r') as arquivo:
                i = int(arquivo.read())
                return i+1
            
        #Se o arquivo não existir inicializará com 0
        except FileNotFoundError:
            matricula = 0
        
        # Atualiza o número da matrícula no arquivo
        with open('matriculas.txt', 'w') as arquivo:
            arquivo.write(str(matricula + 1))

        return matricula + 1
    
    
    #verifica se a tentativa de gravação no arquivo foi executada com sucesso
    def verifica_arquivo(self, parametro, nome_do_arquivo):
        try:
            with open(nome_do_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    if parametro in linha.strip():
                        return True
            return False
        
        except FileNotFoundError:
            return False


    def cad_user(self):
        nome = input("Digite seu nome completo: ")
        nome = self.valida_nome(nome)
        resp = input(f"Seu nome é {nome}?\nDigite 'S' para sim e qualquer outra tecla para reenserir seu nome: ").upper()
        
        if resp == 'S':
            matricula = self.gera_matricula()
            usuario  = f"{nome} - Matrícula: {matricula}\n"

            try:
                with open('nomes.txt','a') as arquivo:
                    arquivo.write(usuario)

                    if self.verifica_arquivo(nome, 'nomes.txt'):
                        print('Gravação realizada com sucesso!')
                    else:
                        print('Erro ao realizar cadastro! ')

            except Exception as e:
                print(f"Ocorreu um erro ao gravar o arquivo: {e}")


        else:
            print("Por favor reescreva seu nome. ")
            self.cad_user()