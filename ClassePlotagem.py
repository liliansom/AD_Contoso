from ClasseAnalise import Analise

# Classe para plotar os dados analisados
class Plotagem:
    def __init__(self):
        self.analise = Analise()

    # Método para plotagem do gráfico de vendas/ loja
    def plotvl(self):
        vl = self.analise.analisar_vendas()
        plt.xticks(rotation=350)
        plt.show()

    # Método para plotagem do gráfico de vendas/ subcategoria de produto
    def plotvp(self):
        vp = self.analise.analisar_produtos()
        vp.plot(kind='pie', figsize=(8,8), autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.show()
