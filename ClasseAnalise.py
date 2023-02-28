from ClasseBusca import Busca

# Classe para analisar as informações do BD
class Analisar:
    def __init__(self):
        self.dados = Busca()

    # Método para analisar vendas por loja
    def analisar_vendas(self):
        # Buscas de tabelas
        tabela_vendas = self.dados.buscar_vendas()
        tabela_lojas = self.dados.buscar_lojas()

        # Mesclar as duas tabelas
        tabela3 = self.dados.mesclar_tabelas(tabela_vendas, tabela_lojas, 'StoreKey')
        self.vendas_lojas = tabela3.groupby('StoreName').sum()
        self.vendas_lojas = self.vendas_lojas[['SalesQuantity']].sort_values('SalesQuantity', ascending=False)
        return self.vendas_lojas

    # Método para analisar vendas por subcategoria
    def analisar_produtos(self):
        # Buscas de tabelas
        tabela_produtos = self.dados.buscar_produtos()
        tabela_vendas = self.dados.buscar_vendas()

        # Mesclar as duas tabelas
        tabela4 = self.dados.mesclar_tabelas(tabela_vendas, tabela_produtos,'ProductKey')
        vendas_por_subcat = tabela4.groupby('ProductSubcategoryName')['SalesQuantity'].sum()
        
        # Mesclar produtos com % < 3%
        pct_vendas_por_subcat = vendas_por_subcat / vendas_por_subcat.sum()
        subcat_menores_4 = pct_vendas_por_subcat[pct_vendas_por_subcat < 0.03]
        vendas_outros = vendas_por_subcat[subcat_menores_4.index].sum()
        vendas_por_subcat['Others'] = vendas_outros
        vendas_por_subcat.drop(subcat_menores_4.index, inplace=True)
        vendas_por_subcat = vendas_por_subcat.sort_values(ascending=False)
        return vendas_por_subcat