class Autor:
    def __init__(self, nome: str, nacionalidade: str, ano_nascimento: int):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.ano_nascimento = ano_nascimento

    def apresentar_dados(self):
        print(f"""Nome do autor: {self.nome}
Nacionalidade do autor: {self.nacionalidade}
Ano de nascimento do autor: {self.ano_nascimento}""")
        
    def obter_descricao(self):
        return f"{self.nome} - {self.nacionalidade}"


class Livro:
    def __init__(self, titulo: str, qtd_paginas: int, ano_publicacao: int, autor: Autor):
        self.titulo = titulo
        self.qtd_paginas = qtd_paginas
        self.ano_publicacao = ano_publicacao
        self.autor = autor

    def apresentar_dados(self):
        print(f"""
Título do livro: {self.titulo}
Quantidade de páginas: {self.qtd_paginas}
Ano de publicação: {self.ano_publicacao}
Descrição do autor: {self.autor.obter_descricao()}
""")
        
def exemplo_livros():

    autor1 = Autor("Machado de Assis", "Brasileiro", 1839)
    autor2 = Autor("Jeff Kinney", "Estadunidense", 1971)
    
    livro1 = Livro("Dom Casmurro", 256, 1899, autor1)
    livro2 = Livro("Diário de um banana", 315, 2006, autor2)

    livro1.apresentar_dados()
    livro2.apresentar_dados()

#================================================================================

class Endereco:
    def __init__(self, rua: str, numero: int, bairro: str, cidade: str, estado: str):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    def apresentar_dados(self):
        print(f"""Rua: {self.rua}
Número: {self.numero}
Bairro: {self.bairro}
Cidade: {self.cidade}
Estado: {self.estado}
""")
    def obter_endereco_completo(self):
        return f"{self.rua} - {self.numero} - {self.bairro} - {self.cidade}/{self.estado}"

class Pessoa:
    def __init__(self, nome: str, endereco: Endereco):
        self.nome = nome
        self.endereco = endereco
    
    def apresentar_dados(self):
        print(f"Nome: {self.nome}")

def exemplo_endereco():
    endereco = Endereco("Silvano Cândido", 3065, "Ponta Aguda", "Blumenau", "SC")
    pessoa = Pessoa("Erick Janzen", endereco)

    pessoa.apresentar_dados()
    print(pessoa.endereco.obter_endereco_completo()) 

exemplo_endereco()
