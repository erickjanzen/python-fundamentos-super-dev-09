class Autor:
    def __init__(self, nome: str, nacionalidade: str, ano_nascimento: int):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.ano_nascimento = ano_nascimento

    def apresentar_dados(self):
        print(f"""Nome do autor: {self.nome}
Nacionalidade do autor: {self.nacionalidade}
Ano de nascimento do autor: {self.ano_nascimento}""")
        
def obter_descricao():
    machado_de_assis = Autor("Machado de Assis", "Brasileiro", 2067)
        
    machado_de_assis.apresentar_dados()

obter_descricao()

class Livro:
    def __init__(self, titulo: str, qtd_paginas: int, ano_publicacao: int, autor: Autor):
        self.titulo = titulo
        self.qtd_paginas = qtd_paginas
        self.ano_publicacao = ano_publicacao
        self.autor = autor
