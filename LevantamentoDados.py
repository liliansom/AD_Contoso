from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io import sql
import pyodbc
from conexao import ConexaoBD

class Levdados:
    def __init__(self):
        self.con = ConexaoBD()
        self.conn = self.con.conexao()
        
    def buscar_vendas(self): 
        self.vendas = 'SELECT * FROM FactSales'
        self.dados_vendas = pd.read_sql(self.vendas, self.conn)
        lista_colunas_vendas = ['StoreKey', 'SalesQuantity', 'ProductKey']
        lista_vendas = self.dados_vendas[lista_colunas_vendas]
        return lista_vendas
        
    def buscar_lojas(self):
        self.lojas = 'SELECT * FROM DimStore'
        self.dados_lojas = pd.read_sql(self.lojas, self.conn)
        lista_colunas_lojas = ['StoreKey', 'StoreName']
        lista_lojas = self.dados_lojas[lista_colunas_lojas]   
        return lista_lojas         

    def buscar_produtos(self):
        self.produtos = 'SELECT * FROM DimProduct'
        self.dados_produtos = pd.read_sql(self.produtos, self.conn)
        lista_colunas_produtos = ['ProductKey', 'ProductSubcategoryKey']
        self.lista_produtos = self.dados_produtos[lista_colunas_produtos]

        self.subcat = 'SELECT * FROM  DimProductSubCategory'
        self.dados_subcat = pd.read_sql(self.subcat, self.conn)
        lista_colunas_subcat = ['ProductSubcategoryKey', 'ProductSubcategoryName']
        self.lista_subcat = self.dados_subcat[lista_colunas_subcat]

        lista_prodcat = self.mesclar_tabelas(self.lista_produtos, self.lista_subcat, 'ProductSubcategoryKey')
        return lista_prodcat

    def mesclar_tabelas(self, tabela1, tabela2, parametro):
        self.tabela1 = tabela1
        self.tabela2 = tabela2
        self.parametro = parametro
        nova_tabela = tabela1.merge(tabela2, on=parametro)
        return nova_tabela

    def analisar_vendas(self):
        lista_vendas = self.buscar_vendas()
        lista_lojas = self.buscar_lojas()
        tabela3 = self.mesclar_tabelas(lista_vendas, lista_lojas, 'StoreKey')
        self.vendas_lojas = tabela3.groupby('StoreName').sum()
        self.vendas_lojas = self.vendas_lojas[['SalesQuantity']].sort_values('SalesQuantity', ascending=False)
        self.vendas_lojas[:5].plot(figsize=(15,5), kind='bar')
        plt.xticks(rotation=350)
        plt.show()
        self.conn.close()
        return self.vendas_lojas



busca = Levdados()
busca.buscar_produtos()
print(busca.buscar_produtos())
