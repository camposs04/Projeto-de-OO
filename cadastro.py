class Cadastro:
    def __init__(self):
        self.usuarios = {}

    def valida_nome(self, nome):
        while (
            not nome.replace(" ", "").isalpha()
            or len(nome) < 6
            or " " not in nome
        ):
            nome = input(
                "Nome inválido! Digite um nome completo (apenas letras, com pelo menos 6 caracteres e um espaço): "
            ).strip()
        return nome

    def gera_matricula(self):
        try:
            with open('matriculas.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
                ultima_matricula = int(linhas[-1]) if linhas else 0
            nova_matricula = ultima_matricula + 1
            with open('matriculas.txt', 'a') as arquivo:
                arquivo.write(f"{nova_matricula}\n")
            return str(nova_matricula)
        except FileNotFoundError:
            with open('matriculas.txt', 'w') as arquivo:
                arquivo.write("1\n")
            return '1'

    def verifica_arquivo(self, parametro, nome_do_arquivo):
        try:
            with open(nome_do_arquivo, 'r') as arquivo:
                names = arquivo.readlines()
                for linha in names:
                    if parametro in linha.strip():
                        return True
            return False
        except FileNotFoundError:
            return False

    def cad_user(self):
        nome = input("\nDigite seu nome completo: ")
        nome = self.valida_nome(nome)
        resp = input(f"\nSeu nome é {nome}?\nDigite 'S' para sim e qualquer outra tecla para reenscrever seu nome: ").upper()
        if resp == 'S':
            matricula = self.gera_matricula()
            self.usuarios[nome] = matricula
            print(f"Cadastro realizado com sucesso! NOME: {nome}, MATRÍCULA: {matricula}")
            try:
                with open('nomes.txt','a') as arquivo:
                    arquivo.write(f"{nome}\n")
                if self.verifica_arquivo(nome, 'nomes.txt'):
                    print('Gravação realizada com sucesso!')
                else:
                    print('Erro ao realizar cadastro! ')
            except Exception as e:
                print(f"Ocorreu um erro ao gravar o arquivo: {e}")
        else:
            print("\nPor favor reescreva seu nome. ")
            self.cad_user()

    def valida_acesso(self, nome, chave_acesso):
        return self.usuarios.get(nome) == chave_acesso
