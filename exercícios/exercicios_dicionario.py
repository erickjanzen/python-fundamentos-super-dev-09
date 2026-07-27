from typing import Dict
from typing import List

def exercicio01():
    pacientes: Dict[str, str | int] = {}
    pacientes["nome_paciente"] = input("Nome do paciente: ")
    pacientes["idade_paciente"] = int(input("Idade do paciente: "))

    print("Paciente: ", pacientes["nome_paciente"], "\nIdade: ", pacientes["idade_paciente"])

def exercicio02():
    aluno: Dict[str, str | int] = {}
    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["idade"] = int(input("Digite a idade do aluno: "))
    aluno["turma"] = input("Digite a turma do aluno: ")
    aluno["curso"] = input("Digite o curso do aluno: ")

    for chave in aluno.keys():
        print(chave)

def exercicio03():
    produtos: Dict[str, str | float | int] = {}
    produtos["nome"] = input("Digite o nome do produto: ")
    produtos["preco"] = float(input("Digite o valor do produto: "))
    produtos["estoque"] = int(input("Digite o estoque do produto: "))
    produtos["categoria"] = input("Digite a categoria do produto: ")

    for valor in produtos.values():
        print(valor)

def exercicio04():
    funcionario: Dict[str, str | int | float] = {}
    funcionario["nome"] = input("Digite o nome do funcionário: ")
    funcionario["cargo"] = input("Digite o cargo do funcionário: ")
    funcionario["salario"] = float(input("Digite o salário do funcionário: "))
    funcionario["setor"] = input("Digite o setor do funcionário: ")

    for item in funcionario.items():
        print(item)

def exercicio05():
    livro: Dict[str, str | int | float] = {}
    livro["titulo"] = input("Digite o título do livro: ")
    livro["autor"] = input("Digite o autor do livro: ")
    livro["ano_publicacao"] = int(input("Digite o ano de publicação: "))
    livro["quantidade_paginas"] = int(input("Digite a quantidade de páginas: "))

    for item in livro.items():
        print(item)

def exercicio06():

    jogos = [
        {
        "nome": "Call Of Duty Modern Warfare 2",
        "genero": "Ação",
        "ano_de_lancamento": "2022",
        "preco": "316,00"
        },
        {
        "nome": "Spider-Man Miles Morales",
        "genero": "Ação",
        "ano_de_lancamento": "2022",
        "preco": "199,90"
        }
    ]
    i = 1
    for jogo in jogos:
        print(f"\nJogo {i}")
        i += 1
        for chave, valor in jogo.items():
            print(f"{chave}: {valor}")

def exercicio07():
    produtos = [
        {
        "id":"01",
        "nome": "Sorvete",
        "categoria": "Doces",
        "preco": 20,
        "estoque": 10
         },
        {
        "id":"02",
        "nome": "iPhone 17",
        "categoria": "Eletrônicos",
        "preco": 6000,
        "estoque": 6},
        {
        "id":"03",
        "nome": "Camiseta CIENA LAB",
        "categoria": "Roupas",
        "preco": 230,
        "estoque": 30
        },
        {
        "id":"04",
        "nome": "Vectra 2000",
        "categoria": "Automóveis",
        "preco": 30000,
        "estoque": 2
        },
        {
        "id":"05",
        "nome": "Boné",
        "categoria": "Roupas",
        "preco": 150,
        "estoque": 15
        }
    ]

    def obter_nomes_produtos():
        nomes = []
        for produto in produtos:
            nomes.append(produto["nome"])
        print(nomes)

    obter_nomes_produtos()

    def obter_produtos_com_estoque_baixo():
        produtos_estoque_baixo = []
        for produto in produtos:
            if produto["estoque"] < 10:
                produtos_estoque_baixo.append(produto["nome"])

        print(f"Produtos com estoque abaixo de 10: {produtos_estoque_baixo}")
    
    obter_produtos_com_estoque_baixo()

    def obter_produtos_por_categoria():
        produtos_filtrados = []
        produto_procurado = input("Pesquise uma categoria: ").capitalize()
        for produto in produtos:
            if produto["categoria"] == produto_procurado:
                produtos_filtrados.append(produto["nome"])
        print("Produtos filtrados: ", produtos_filtrados)
    obter_produtos_por_categoria()

exercicio07()


 # i = 1
 # for produto in produtos:
        #     print(f"\nProduto: {i}")
        #     i += 1
        #     for chave, valor in produto.items():
        #         print(f"{chave}: {valor}")