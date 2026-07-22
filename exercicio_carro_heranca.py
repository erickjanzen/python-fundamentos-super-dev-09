class Carro:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def apresentar_dados(self):
        print(f"""
Marca: {self.marca}
Modelo: {self.modelo}""")

class Combustivel(Carro):
    def __init__(self, marca: str, modelo: str, cilindrada: float, potencia: int):
        super().__init__(self, marca, modelo)
        self.cilidrada = cilindrada
        self.potencia = potencia

    def apresentar_dados(self):
        super().apresentar_dados()
        print(f"""Cilindrada: {self.cilindrada}
Potência: {self.potencia} CV
""")

class Gasolina(Combustivel):
    def __init__(self, marca: str, modelo: str, tipo_combustivel: str):
        super().__init__(self, marca, modelo)
        self.tipo_combustivel = tipo_combustivel