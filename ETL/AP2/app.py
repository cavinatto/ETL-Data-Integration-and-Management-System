# %%
#-------------------------------------------------
# importar módulos 
# sys - forncesse acesso a variável e funções
# importlib - importa m´dulos dinamicamente
# porquê não estava achando o models
# ModuleNotFoundError

#import modelos
import env  
from modelos.models import Produto

import sys
import importlib
import openpyxl
import pandas as pd
import sqlalchemy as sql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from etl.etl import ETL

module_name = "models"
module_dir = "C:\\Users\\arfur\\Downloads\\AP2 (1)\\AP2\\modelos"

sys.path.append(module_dir)

try:
    models = importlib.import_module(module_name)
    print("Módulo carregado com sucesso!")
except ImportError as e:
    print(f"Erro ao carregar o módulo: {e}")
    
module_name = "env"
module_dir = "C:\\Users\\arfur\\Downloads\\AP2 (1)\\AP2\\env.py"

sys.path.append(module_dir)

try:
    env = importlib.import_module(module_name)
    print("Módulo carregado com sucesso!")
except ImportError as e:
    print(f"Erro ao carregar o módulo: {e}")
#------------------------------------------------- fim
  
#%%

# Criar uma conexão com o banco de dados
engine = create_engine('sqlite:///banco_de_dados.db')
Session = sessionmaker(bind=engine)
session = Session()

# %%

# Ler o arquivo Excel df(dataframe)
dfSC = pd.read_excel("dados_iniciais.xlsx", sheet_name="StatusClinete")
print(dfSC.to_string(index=False))

dfPr = pd.read_excel("dados_iniciais.xlsx", sheet_name="Produto")
print(dfPr.to_string(index=False))

dfCli = pd.read_excel("dados_iniciais.xlsx", sheet_name="Cliente")
print(dfCli.to_string(index=False))

dfPe = pd.read_excel("dados_iniciais.xlsx", sheet_name="Pedido")
print(dfPe.to_string(index=False))

dfItPe = pd.read_excel("dados_iniciais.xlsx", sheet_name="ItemPedido")
print(dfItPe.to_string(index=False))

dfCa = pd.read_excel("dados_iniciais.xlsx", sheet_name="Categoria")
print(dfCa.to_string(index=False))


#%%


#instanciando etl
etl = ETL(db_url="sqlite:///banco_de_dados.db", file_path="dados_iniciais.xlsx")

print("Digite as infiormações: ")

while True:
    id = input("ID: ")
    if id.strip() != "":
        break
    else:
        print("Erro: ID não pode ser vazio")

while True:
    nome = input("Nome: ")
    if nome.strip() != "":
        break
    else:
        print("Erro: Nome não pode ser vazio")

while True:
    categoria = input("Categoria: ")
    if categoria.strip() != "":
        break
    else:
        print("Erro: Categoria não pode ser vazia")

while True:
    preco = input("Preço: ")
    if preco.replace('.', '', 1).isdigit():
        break
    else:
        print("Erro: Preço deve ser um número flutuante")

p = Produto(id, nome, categoria, preco)

#%%   
try:

   extracted_data = etl.extract()      # Extrair dados do Excel

    
   transformed_data = etl.transform(extracted_data) # Transforma os dados para o formato de tabelas

   etl.load(transformed_data)  # Carregua os dados no bd

   Base.metadata.create_all(etl.engine)  # Cria tabelas conforme as classes importadas

   print("ETL concluído com sucesso!")
   
   
# except é bloco associado atry, porém não está no bloco, pois é executado apenas na exceção, sendo assim fica fora da dentação    
except Exception as e: 
    print(f"Erro durante o processo ETL: {e}")
# %%
