def exercicio01():
    print("Bem vindo")
    for i in range(0, 4):
        print("Bem vindo")


def exercicio02():
    for i in range(15,31):
        print(i)


def exercicio03():
    numero: int = int(input("Digite um número inteiro: "))
    for i in range (1, 11):
        print(f"{numero} x {i} = {numero * i}")


def exercicio04():
    i = 0
    soma = 0
    for i in range (0, 5):
        numero: int = int(input("Digite um número: "))
        soma = numero + soma
    print(f"Soma total: {soma}")


exercicio04()