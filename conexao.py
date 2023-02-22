import pyodbc

class Retornar_conexao:
    def conexao(self):
        dadosconex= "Driver={SQL Server};Server=.;Database=ContosoRetailDW;"
        conexao = pyodbc.connect(dadosconex)
        return conexao
    

    
    