class Imoveis:
    proprietario = ""
    taxa_admin_mensal = 1
    taxa_admin_anual = 2


class Aluguel:
    def __init__ (self):
        self.imoveis = Imoveis()
        self.taxa_mensal = self.imoveis.taxa_admin_mensal

    def cobrar(self):
        print(self.taxa_mensal)
        taxa_admin_anual = 0

aluguel = Aluguel()
valor_mensal = aluguel.taxa_mensal
print(valor_mensal)