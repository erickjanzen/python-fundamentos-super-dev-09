def exercicio_01_mensagens():
    print("Bem-vindo!")
    print("Estou aprendendo Python")
    print("O Python é usado para criar programas")


def exercicio_02_variaveis():
    nome: str = input("Digite o seu nome: ")
    idade: int = input("Digite a sua idade: ")
    cidade: str = input("Digite a sua cidade: ")
    print(f"Seu nome é: {nome}\nSua idade é: {idade}\nSua cidade é: {cidade}")


def exercicio_03_input_nome():
    nome: str = input("Digite o seu nome: ")
    print(f"Olá, {nome.capitalize()}! Seja bem vindo ao sistema.")


def exercicio_04_dados_pessoais():
    nome: str = input("Digite o seu nome: ")
    bairro: str = input("Digite o seu bairro: ")
    cidade: str = input("Digite a sua cidade: ")
    print(f"{nome.capitalize()} mora no bairro {bairro.title()}, na cidade de {cidade.title()}")


def exercicio_05_idade_int():
    idade: int = int(input("Digite sua idade"))
    print(f"Sua idade é: {idade}")


def exercicio_06_idade_proximo_ano():
    idade: int = int(input("Digite a sua idade: "))
    proximaIdade: int = idade + 1
    print(f"Sua idade ano que vem será: {proximaIdade}")


def exercicio_07_dobro_numero():
    numero: int = int(input("Digite um número inteiro: "))
    dobroDoNumero: int = numero * 2
    print(f"O dobro do numero é {dobroDoNumero}")


def exercicio_08_maioridade():
    idade: int = int(input("Digite a sua idade: "))
    if idade < 18:
        print("Você é menor de idade")
    else:
        print("Você é maior de idade")


def exercicio_09_numero_positivo():
    numero: int = int(input("Digite um número: "))
    if numero < 0:
        print("O seu número é negativo")
    elif numero > 0:
        print("O seu número é positivo")
    else:
        print("O seu número é nulo")


def exercicio_10_entrada_evento():
    nome: str = input("Digite o nome do usuário: ")
    idade: int = int(input("Digite a idade do usuário: "))
    if idade > 15:
        print(f"{nome.capitalize()}, você pode entrar no evento")
    else:
        print(f"{nome.capitalize()}, você não pode entrar no evento")

    
exercicio_10_entrada_evento()