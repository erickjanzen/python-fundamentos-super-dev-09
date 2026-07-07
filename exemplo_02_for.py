# Padrão de nomenclatura
# nome funções          snake_case
# nome de parâmetros    snake_case
# nome de variáveis     snake_case

from pathlib import Path


def exemplo_01():
    # range é utilizado para ir de um ponto até outro, neste caso ir de 0 até 4
    for i in range(0, 5):
        print("Olá mundo")


def exemplo_02():
    # cwd é utlizado para pegar o diretório atual da execução do python
    diretorio_atual = Path.cwd()
    nome_novo_diretorio = "Arquivos"
    caminho_novo_diretorio = diretorio_atual / nome_novo_diretorio
    # C: \Users\


def exemplo_03_listar():
    # criar lista vazia
    filmes = []
    filmes.append("Filho do Alanzoka o Filme") # Posição 0
    filmes.append("As branquelas") # Posição 1
    filmes.append("Jumangi") # Posição 2
    filmes.append("Star Wars") # Posição 3
    filmes.append("The Amazing Spider-Man") # Posição 4

    # Alterar o nome do filme na posição 2
    filmes[2] = "Jumanji"

    filmes.remove("Star Wars") # Posição 3
    print("Tamanho da lista de filmes: ", len(filmes))

    print("Filmes")
    # for normal
    for i in range(0, len(filmes)):
        filme = filmes[i]
        print(filme)

    # foreach
    for filme in filmes:
        print(filme)


def solicitar_dados_armazenando_vetor():
    numeros = []
    for i in range(0, 5):
        numero_da_sorte = int (input("Digite o número: "))
        # Adicionar o número digitado pelo usuário na lista
        numeros.append(numero_da_sorte)

    soma = 0
    #Percorrer o vetor (lista)
    for i in range(0, 5):
        soma = soma + numeros[i]

    quantidade_pares = 0
    # Percorrer a lista
    for i in range(0, 5):
        # Verificando se o resto da divisão é 0, o número é par
        if numeros[i] % 2 == 0:
            quantidade_pares = quantidade_pares + 1

    print ("Quantidade de pares: " + str(quantidade_pares))
    print("Soma: " + str(soma))


solicitar_dados_armazenando_vetor()