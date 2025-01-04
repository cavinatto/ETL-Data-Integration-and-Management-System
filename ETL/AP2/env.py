import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from abc import ABC, abstractmethod
from modelos.models import Base, Produto, Cliente, Pedido, ItemPedido

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
        except FileNotFoundError:
            raise FileNotFoundError(f"O arquivo '{self.file_path}' não foi encontrado.")
        except ValueError as e:
            raise ValueError(f"Erro ao ler o arquivo Excel: {e}")
        except Exception as e:
            raise Exception(f"Erro desconhecido durante a extração: {e}")

    def transform(self, data):
        """Transforma os dados para o formato esperado pelas tabelas."""
        try:
            required_sheets = ["Produtos", "Clientes", "Pedidos", "ItensPedido"]
            for sheet in required_sheets:
                if sheet not in data:
                    raise KeyError(f"A planilha '{sheet}' está faltando no arquivo.")

            transformed_data = {
                "produtos": data["Produtos"].to_dict(orient="records"),
                "clientes": data["Clientes"].to_dict(orient="records"),
                "pedidos": data["Pedidos"].to_dict(orient="records"),
                "itens_pedido": data["ItensPedido"].to_dict(orient="records"),
            }
            return transformed_data
        except KeyError as e:
            raise KeyError(f"Erro na transformação dos dados: {e}")
        except Exception as e:
            raise Exception(f"Erro desconhecido durante a transformação: {e}")

    def load(self, transformed_data):
        """Carrega os dados no banco de dados."""
        session = self.Session()
        try:
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
        except SQLAlchemyError as e:
            session.rollback()
            raise ValueError(f"Erro ao carregar os dados no banco de dados: {e}")
        except Exception as e:
            session.rollback()
            raise Exception(f"Erro desconhecido durante o carregamento: {e}")
        finally:
            session.close()

# Exemplo de uso:
if __name__ == "__main__":
    db_url = "sqlite:///banco_de_dados.db"  # URL do banco de dados
    file_path = "dados_iniciais.xlsx"       # Caminho do arquivo Excel

    etl = ETL(db_url=db_url, file_path=file_path)
    try:
        extracted_data = etl.extract()
        transformed_data = etl.transform(extracted_data)
        etl.load(transformed_data)
        print("ETL concluído com sucesso!")
    except Exception as e:
        print(f"Erro durante o processo ETL: {e}")
