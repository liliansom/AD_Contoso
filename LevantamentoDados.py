import pandas as pd
from pandas.io import sql
import pyodbc
from conexao import Retornar_conexao

class Dados:
    def __init__(self):
        self.con = Retornar_conexao()
        self.conn = self.con.conexao()
    
    def buscar_dados(self): 
        self.sql = 'SELECT TOP 10 * FROM FactSales'
        self.dados = sql.read_sql(self.sql, self.conn)
        dados1 = self.dados.head(10)
        print(f'{dados1}')

                            
dados = Dados()
dados.buscar_dados()