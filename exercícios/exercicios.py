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

    
def exercicio_11_verificar_nota():
    nota: float = float(input("Digite a nota do aluno: "))
    if nota < 7:
        print("Aluno reprovado")
    else:
        print("Aluno aprovado")


def exercicio_12_verificar_saldo():
    saldo: float = float(input("Digite o saldo disponível: "))
    valor: float = float(input("Digite o valor da compra: "))
    if saldo > valor:
        print("Compra aprovada")
    else:
        print("Saldo insuficiente")


def exercicio_13_aprovacao_nota_frequencia():
    nota: float = float(input("Digite a nota do aluno: "))
    frequencia: int = int(input("Digite a frequência do aluno: "))
    if nota >= 7 and frequencia >= 75:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")


def exercicio_14_entrada_gratuita():
    idade: int = int(input("Digite a idade do usuário: "))
    if idade < 7 or idade > 59:
        print("Entrada gratuita.")
    else:
        print("Entrada paga.")


def exercicio_15_login_simples():
    usuario: str = input("Digite o nome do usuário: ")
    senha: str = input("Digite a senha do usuário: ")
    if usuario == "admin" and senha == "1234":
        print("Login realizado com sucesso")
    else:
        print("Usuário ou senha incorreta")


def exercicio_16_mensagem_varias_vezes():
    i = 0
    while i < 5:
        print("Estou aprendendo Python")
        i += 1


def exercicio_17_numeros_pares():
    i = 2
    while i < 21:
        print(i)
        i = i + 2


def exercicio_18_repetir_mensagem():
    mensagem: str = input("Digite uma mensagem: ")
    quantidade: int = int(input("Digite a quantidade de vezes que a mensagem irá aparecer: "))
    i = 0
    while i < quantidade:
        print(mensagem)
        i += 1

def exercicio_19_somar_1_ate_n():
    numero: int = int(input("Digite um número: "))
    i = 0
    soma: int = 0
    while i < numero:
        i += 1
        soma = i + soma
    print(soma)


def exercicio_20_senha_while():
    senha: str = input("Digite a senha: ")
    while senha != "angrybirds":
        senha: str = input("Senha incorreta, tente novamente: ")
    print("Acesso permitido")


def exercicio_21_menu_simples():
    menu: str = input("[1] - Mostrar mensagem de boas-vindas\n[2] - Mostrar mensagem sobre Python\n[0] - Sair\n")
    while menu != 0:
        if menu == "1":
            print("Bem-vindo!")
            menu: str = input("[1] - Mostrar mensagem de boas-vindas\n[2] - Mostrar mensagem sobre Python\n[0] - Sair\n")
        elif menu == "2":
            print("Python é uma linguagem de programação")
            menu: str = input("[1] - Mostrar mensagem de boas-vindas\n[2] - Mostrar mensagem sobre Python\n[0] - Sair\n")
        elif menu == "0":
            return
        else:
            menu: str = input("[1] - Mostrar mensagem de boas-vindas\n[2] - Mostrar mensagem sobre Python\n[0] - Sair\nOpção inválida, digite uma das opções acima\n")


def exercicio_22_tabuada_while():
    numero: int = int(input("Digite um número para tabuada: "))
    i = 1
    while i < 11:
        print(f"{numero} x {i} = {numero * i}")
        i += 1


def exercicio_23_somar_ate_zero():
    menu: int = 1
    soma: int = 0
    while menu != 0:
        menu: int = int(input("Digite um número para somar\nDigite 0 para finalizar soma\n"))
        soma = menu + soma
    print(f"Soma final: {soma}")


def exercicio_24_contar_positivos():
    numero: int = 1
    positivos: int = 0
    while numero != 0:
        numero: int = int(input("Digite um número diferente de 0: "))
        if numero > 0:
            positivos = positivos + 1
    print(f"{positivos} números digitados são positivos")


def exercicio_25_maior_numero():
    maiorNumero: int = 0
    i = 0
    while i < 5:
        numero: int = int(input("Digite um número inteiro: "))
        if numero > maiorNumero:
            maiorNumero = numero
        i += 1
    print(f"O maior número digitado foi {maiorNumero}")

exercicio_25_maior_numero()
