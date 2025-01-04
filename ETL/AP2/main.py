# %%
# imports
import os

from dotenv import load_dotenv

from etl.etl import ETL

load_dotenv()

# %%
# conexão com o banco de dados
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
host = os.getenv("HOST")
banco_de_dados = os.getenv("BANCO_DE_DADOS")

# %%
# testando o ETL
origem = "dados_iniciais.xlsx"
destino = f"mssql+pyodbc://{usuario}:{senha}@{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server"
etl = ETL(origem, destino)

etl.extract()
etl.transform()
etl.load()

