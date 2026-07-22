class Pessoa:
    def __init__(self, nome: str, numero_telefone: str, email: str):
        self.nome = nome
        self.numero_telefone = numero_telefone
        self.email = email

    def apresentar_dados(self):
        print(f"""
Nome: {self.nome}
Número de telefone: {self.numero_telefone}
Email: {self.email}""")

class Professor(Pessoa):
    def __init__(self, nome: str, numero_telefone: str, email: str, salario: float):
        super().__init__(nome, numero_telefone, email)
        self.salario = salario

    def apresentar_dados(self):
        super().apresentar_dados()
        print(f"Salário: {self.salario}")

class Aluno(Pessoa):
    def __init__(self, nome: str, numero_telefone: str, email: str, nota1: float, nota2: float, nota3: float):
        super().__init__(nome, numero_telefone, email)
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def apresentar_dados(self):
        super().apresentar_dados()
        print(f"""
Nota 1: {self.nota1}
Nota 2: {self.nota2}
Nota 3: {self.nota3}
""")
        self.calcular_media()

    def calcular_media(self):
        media = (self.nota1 + self.nota2 + self.nota3) / 3
        print(f"Média: {media:.2f}")

def exemplo_pessoa():
    pessoa = Pessoa("Arthur Morgan", "1234", "arthurmorgan@rd.com")
    professor = Professor("Elvis Presley", "58494", "elvis@rd.com", 150)
    aluno1 = Aluno("Coringa Junior", "42984298", "coringasafadinho@baidu.com", 7, 3, 9)
    aluno2 = Aluno("Batman Junior", "74298498", "batmanserio@avast.com", 9, 8, 10)

    pessoa.apresentar_dados()
    separador()
    professor.apresentar_dados()
    separador()
    aluno1.apresentar_dados()
    separador()
    aluno2.apresentar_dados()
    separador()

def separador():
    print("====================================================================================================================")

exemplo_pessoa()