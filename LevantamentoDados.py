from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io import sql
import pyodbc
from conexao import Retornar_conexao

class Levdados:
    def __init__(self):
        self.con = Retornar_conexao()
        self.conn = self.con.conexao()
        
    def buscar_vendas(self): 
        self.vendas = 'SELECT * FROM FactSales'
        self.dados_vendas = pd.read_sql(self.vendas, self.conn)
        lista_colunas_vendas = ['StoreKey', 'SalesQuantity']
        lista_vendas = self.dados_vendas[lista_colunas_vendas]
        return lista_vendas
        
    def buscar_lojas(self):
        self.lojas = 'SELECT StoreKey, StoreName FROM DimStore'
        self.dados_lojas = pd.read_sql(self.lojas, self.conn)
        lista_lojas = self.dados_lojas      
        return lista_lojas         


