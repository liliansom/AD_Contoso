from IPython.display import display
import pandas as pd
from pandas.io import sql
import pyodbc
from conexao import ConexaoBD


# Classe para integração com Banco de Dados e busca de informações
class Busca:
    def __init__(self):
        self.con = ConexaoBD()
        self.conn = self.con.conexao()
    
    # Método para fazer levantamento de informações de vendas no banco de dados
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

        tabela_prodcat = self.mesclar_tabelas(self.tabela_produtos, self.tabela_subcat, 'ProductSubcategoryKey')
        return tabela_prodcat

    #Método para mesclar tabelas
    def mesclar_tabelas(self, tabela1, tabela2, parametro):
        self.tabela1 = tabela1
        self.tabela2 = tabela2
        self.parametro = parametro
        nova_tabela = tabela1.merge(tabela2, on=parametro)        
        return nova_tabela


