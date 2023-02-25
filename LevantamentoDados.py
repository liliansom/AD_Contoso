from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io import sql
import pyodbc
from conexao import ConexaoBD

# Classe para buscar informações no Banco de Dados
class Busca:
    def __init__(self):
        self.con = ConexaoBD()
        self.conn = self.con.conexao()
    
    # Método para fazer busca de vendas no banco de dados
    def buscar_vendas(self): 
        self.vendas = 'SELECT * FROM FactSales'
        self.dados_vendas = pd.read_sql(self.vendas, self.conn)
        lista_colunas_vendas = ['StoreKey', 'SalesQuantity', 'ProductKey']
        tabela_vendas = self.dados_vendas[lista_colunas_vendas]
        return tabela_vendas

    # Método para fazer busca de lojas no banco de dados    
    def buscar_lojas(self):
        self.lojas = 'SELECT * FROM DimStore'
        self.dados_lojas = pd.read_sql(self.lojas, self.conn)
        lista_colunas_lojas = ['StoreKey', 'StoreName']
        tabela_lojas = self.dados_lojas[lista_colunas_lojas]   
        return tabela_lojas         

    # Método para fazer busca de produtos no banco de dados
    def buscar_produtos(self):
        self.produtos = 'SELECT * FROM DimProduct'
        self.dados_produtos = pd.read_sql(self.produtos, self.conn)
        lista_colunas_produtos = ['ProductKey', 'ProductSubcategoryKey']
        self.tabela_produtos = self.dados_produtos[lista_colunas_produtos]

        self.subcat = 'SELECT * FROM  DimProductSubCategory'
        self.dados_subcat = pd.read_sql(self.subcat, self.conn)
        lista_colunas_subcat = ['ProductSubcategoryKey', 'ProductSubcategoryName']
        self.tabela_subcat = self.dados_subcat[lista_colunas_subcat]

        tabela_prodcat = self.mesclar_tabelas(self.lista_produtos, self.lista_subcat, 'ProductSubcategoryKey')
        return tabela_prodcat

    #Método para mesclar tabelas
    def mesclar_tabelas(self, tabela1, tabela2, parametro):
        self.tabela1 = tabela1
        self.tabela2 = tabela2
        self.parametro = parametro
        nova_tabela = tabela1.merge(tabela2, on=parametro)
        return nova_tabela

# Classe para analisar as informações do BD
class Analise:
    def __init__(self):
        self.dados = Busca()

    # Método para analisar vendas por loja
    def analisar_vendas(self):
        tabela_vendas = self.dados.buscar_vendas()
        tabela_lojas = self.dados.buscar_lojas()
        tabela3 = self.dados.mesclar_tabelas(tabela_vendas, tabela_lojas, 'StoreKey')
        self.vendas_lojas = tabela3.groupby('StoreName').sum()
        self.vendas_lojas = self.vendas_lojas[['SalesQuantity']].sort_values('SalesQuantity', ascending=False)
        self.vendas_lojas[:5].plot(figsize=(15,5), kind='bar')
        return self.vendas_lojas

    # Método para analisar vendas por subcategoria
    def analisar_produtos(self):
        tabela_produtos = self.dados.buscar_produtos()
        tabela_vendas = self.dados.buscar_vendas()
        tabela4 = self.dados.mesclar_tabelas(tabela_vendas, tabela_produtos,'ProductKey')
        vendas_por_subcat = tabela4.groupby('ProductSubcategoryName')['SalesQuantity'].sum()
        # Mesclar produtos com % < 4%
        pct_vendas_por_subcat = vendas_por_subcat / vendas_por_subcat.sum()
        subcat_menores_4 = pct_vendas_por_subcat[pct_vendas_por_subcat < 0.04]
        vendas_outros = vendas_por_subcat[subcat_menores_4.index].sum()
        vendas_por_subcat['Others'] = vendas_outros
        vendas_por_subcat.drop(subcat_menores_4.index, inplace=True)
        vendas_por_subcat = vendas_por_subcat.sort_values(ascending=False)
        return vendas_por_subcat

# Classe para plotar os dados analisados
class Plotagem:
    def __init__(self):
        self.analise = Analise()

    # Método para plotagem do gráfico de vendas/ loja
    def plotvl(self):
        vl = self.analise.analisar_vendas()
        plt.xticks(rotation=350)
        plt.show()
        self.conn.close()

    # Método para plotagem do gráfico de vendas/ subcategoria de produto
    def plotvp(self):
        vp = self.analise.analisar_produtos()
        vp.plot(kind='pie', figsize=(8,8), autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.show()
        self.conn.close()

busca = Plotagem()
busca.plotvl()

