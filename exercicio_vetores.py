def execicio05():
    nomes = []
    nomes.append("Erick")
    nomes.append("Mateus")
    nomes.append("Elias")
    nomes.append("Ana")
    nomes.append("Lucas")

    print (f"{nomes[0]}, {nomes[1]}, {nomes[2]}, {nomes[3]}, {nomes[4]}")


def exercicio06():
    frutas = []
    i = 0
    while i < 3:
        fruta = input("Digite uma fruta: ")
        frutas.append(fruta)
        i += 1
    print(f"{frutas[0]}, {frutas[1]}, {frutas[2]}")


def exercicio07():
    numeros = []
    i = 0
    while i < 4:
        numero = input("Digite um número: ")
        numeros.append(numero)
        i += 1
    
    print("Números digitados: ")
    print(f"Primeiro número:    {numeros[0]}")
    print(f"Segundo número:     {numeros[1]}")
    print(f"Terceiro número:    {numeros[2]}")
    print(f"Quarto número:      {numeros[3]}")

def exercicio08():
    notas: float = []
    i = 0
    while i < 4:
        nota = float(input("Digite a nota: "))
        notas.append(nota)
        i += 1


    print(notas)
    print(f"Primeira nota: {notas[0]}")
    print(f"Última nota: {notas[3]}")
    notas[1] = float(10)
    print(f"Segunda nota alterada: {notas[1]}")
    notas.remove(notas[2])

    i = 0
    soma: float = 0
    while i < len(notas):
        soma = notas[i] + soma
        i += 1

    print(f"Tamanho: {len(notas)}")
    print(f"Média: {soma / len(notas)}")


def exercicio09():
    nomes = []
    for i in range(0, 5):
        nome = input("Digite um nome: ")
        nomes.append(nome)

    for i in range(0, 5):
        print(nomes[i].capitalize())


def exercicio10():
    frutas = []
    for i in range(0, 5):
        fruta = input("Digite uma fruta: ")
        frutas.append(fruta)

    print("Frutas cadastradas:")
    for i in range(0, len(frutas)):
        print(frutas[i].capitalize())


def exercicio11():
    numeros: int = []
    soma: int = 0
    for i in range(0, 5):
        numero = int(input("Digite um número: "))
        numeros.append(numero)

    for i in range(0, len(numeros)):
        soma = numeros[i] + soma


    print(f"\nNúmeros selecionados: {numeros}")
    print(f"Soma dos números: {soma}")
    
def exercicio12():
    numeros: int = []
    pares: int = 0
    for i in range(0, 6):
        numero: int = input("Digite um número: ")
        numeros.append(numero)
    
    for i in range(0, len(numeros)):
        if int(numeros[i]) % 2 == 0:
            pares = pares + 1

    print(f"Números digitados: {numeros}")
    print(f"Quantidade de números pares: {pares}")


def exercicio13():
    notas: float = []
    soma: float = 0
    for i in range(0, 4):
        nota = float(input("Digite uma nota: "))
        notas.append(nota)
        soma = nota + soma
    
    media = soma / len(notas)

    status = ""

    if media >= 7:
        status = "Aprovado"
    else:
        status = "Reprovado"

    print(f"Notas: {notas}")
    print(f"Média: {media}")
    print(f"Status: {status}")

exercicio13()