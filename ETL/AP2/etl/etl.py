#%%

#_________________________________
# adicona diretório pai a uma array
# sys.path porcura por diretório
# os.path.abspath retorna caminho absoluto
# os.path.join junta caminhos
# os.path.diname retorna
# porque não lia o diretório
#______________________________

import sys
import importlib
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from abc import ABC, abstractmethod
from modelos.base import Base 
from modelos.models import StatusCliente, Produto, Cliente, Pedido, ItemPedido


#%%
# Classe abstrata base (deve ser implementada no sistema previamente)
class AbstractETL(ABC):
    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    @abstractmethod
    def load(self, transformed_data):
        pass

#%%
class ETL(AbstractETL):
    def __init__(self, db_url, file_path):
        self.db_url = db_url
        self.file_path = file_path
        self.engine = create_engine(self.db_url)
        self.Session = sessionmaker(bind=self.engine)

    def extract(self):
        """Extrai dados do arquivo Excel."""
        try:
            data = pd.read_excel(self.file_path, sheet_name=None)  # Lê todas as planilhas
            return data
        except Exception as e:
            raise ValueError(f"Erro ao extrair dados do arquivo: {e}")

    def transform(self, data):
        """Transforma os dados para o formato esperado pelas tabelas."""
        try:
            transformed_data = {
                "produtos": data["Produtos"].to_dict(orient="records"),
                "clientes": data["Clientes"].to_dict(orient="records"),
                "pedidos": data["Pedidos"].to_dict(orient="records"),
                "itens_pedido": data["ItensPedido"].to_dict(orient="records"),
            }
            return transformed_data
        except KeyError as e:
            raise ValueError(f"Tabela esperada não encontrada no arquivo: {e}")

    def load(self, transformed_data):
        """Carrega os dados no banco de dados."""
        try:
            session = self.Session()
            # Inserção de dados nas tabelas na ordem correta para evitar conflitos de FK
            for produto in transformed_data["produtos"]:
                session.add(Produto(**produto))
            
            for cliente in transformed_data["clientes"]:
                session.add(Cliente(**cliente))
            
            for pedido in transformed_data["pedidos"]:
                session.add(Pedido(**pedido))
            
            for item in transformed_data["itens_pedido"]:
                session.add(ItemPedido(**item))

            session.commit()
        except Exception as e:
            session.rollback()
            raise ValueError(f"Erro ao carregar dados no banco de dados: {e}")
        finally:
            session.close()

# Exemplo de uso:
if __name__ == "__main__":
    db_url = "sqlite:///banco_de_dados.db"  # URL do banco de dados
    file_path = "dados_iniciais.xlsx"       # Caminho do arquivo Excel

    etl = ETL(db_url=db_url, file_path=file_path)
    extracted_data = etl.extract()
    transformed_data = etl.transform(extracted_data)
    etl.load(transformed_data)

#%%    
#tabelas
#transforma
#carrega

df = pd.read_excel("dados_iniciais.xlsx")
df_formato = df.to_string(index=False)
df_formato.to.excel('dados_iniciais_formatado.xlsx', index=False)

