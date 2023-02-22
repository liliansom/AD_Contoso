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
        self.dados

                            
dados = Dados()
dados.buscar_dados()