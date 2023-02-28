from ClasseAnalise import Analisar
import matplotlib.pyplot as plt


# Classe para plotar os dados analisados
class Plotagem:
    def __init__(self):
        self.analise = Analisar()

    # Método para plotagem do gráfico de vendas/ loja
    def plotvl(self):
        vl = self.analise.analisar_vendas()
        self.vendas_lojas[:5].plot(figsize=(15,5), kind='bar')
        plt.xticks(rotation=350)
        plt.show()

    # Método para plotagem do gráfico de vendas/ subcategoria de produto
    def plotvp(self):
        vp = self.analise.analisar_produtos()
        vp.plot(kind='pie', figsize=(8,8), autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.show()
        self.conn.close()