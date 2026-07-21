class Pessoa:
    def __init__(self, nome: str, sobrenome: str):
        self.nome = nome
        self.sobrenome = sobrenome

    def gerar_nome_completo(self):
        return f"{self.nome} {self.sobrenome}"
    

# herança(inheritance) permite uma classe (filha) herdar da classe pai
class Funcionario(Pessoa):
    def __init__(self, nome: str, sobrenome: str, cargo: str):
        # super() permite ter acesso a propriedades e funções da classe pai
        super().__init__(nome, sobrenome)
        self.cargo = cargo

    
def exemplo_funcionario():
    pessoa = Pessoa("Ronaldo", "Femomeno")
    print("Nome completo:", pessoa.gerar_nome_completo())

    funcionario = Funcionario("Lionel", "Messi", "Administrativo")
    print("Nome completo do funcionário:", funcionario.gerar_nome_completo())

exemplo_funcionario()

"""
Criar uma classe Pessoa com os seguintes dados:
    - nome
    - numero telefone
    - email
    criar uma função par apresentar todos os dados

criar uma classe professor com os seguintes dados
    - nome
    - numero telefone
    - email
    - salario

    herança de Pessoa
    criar uma função para apresenar todos os dados

criar uma classe aluno com os seguintes dados: 
    - nome
    - numero telefone
    - email
    - nota 1
    - nota 2
    - nota 3

    herança de pessoa
    criar uma função para apresentar todos os dados
    criar uma função para apresentar a média
"""