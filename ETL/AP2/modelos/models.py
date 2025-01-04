#%%
import sys
import importlib
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import enum

# --importando a classe Base--#
from modelos.base import Base 
# -- -- #

#dataframe
from sqlalchemy import create_engine
import pandas
#fim data


#%%
Base = declarative_base()

# Enum para status do cliente
class StatusCliente(enum.Enum):
    
    def __init__(self, nome:str):
        self.__nome = nome
    
    BOM = "bom"
    MEDIO = "médio"
    RUIM = "ruim"
    
    def limitestatus(self)->int:
        if nome == BOM: Cliente.limite_credito = 150.00
        elif nome == MEDIO : Cliente.limite_credito = 90.00
        else: Cliente.limite_credito= 45.00


#%%  
# Modelo Produto
class Produto(Base):
    
    def __init__(self, codigo:int, nome:str, preco:float, nome_categoria:str):
        self.nome=nome
        self.__codigo = codigo
        self._preco = preco
        self.nome_categoria = nome_categoria
        
   
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    categoria = Column(String(50), nullable=False)
    preco = Column(Float, nullable=False)
    

#%%
# Modelo Cliente
class Cliente(Base):
    
    def __init__(self, codigo:int, nome:str, endereco:str, telefone:str, nome_status:str):
        self.__codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.limite_credito = StatusCliente.get_limite_credito(nome_status) #quero que o limite esteja relacionado ao status
        self.nome_status = nome_status
    
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    endereco = Column(String(255), nullable=False)
    telefone = Column(String(20), nullable=False)
    status = Column(Enum(StatusCliente), nullable=False)
    limite_credito = Column(Float, nullable=False)


#%%
# Modelo Pedido
class Pedido(Base):
    
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    data = Column(Date, nullable=False)
    cliente = relationship("Cliente", back_populates="pedidos")
    itens = relationship("ItemPedido", back_populates="pedido")
    
    def __init__(self, id:int, cliente_id:int, data:str, cliente:str, itens:str):
        self.__id= id
        self.__cliente_id = cliente_id
        self.data = data
        self.itens = itens
        

#%%
# Modelo ItemPedido
class ItemPedido(Base):
    
    def __init__(self, id:int, pedido_id:int, produto_id:int, quantidade:int, pedido:str, produto:str):
        self.__id = id
        self.pedido = pedido
        self.__produto_id = produto_id
        self.quantidade = quantidade
        self.__pedido = pedido
        self.produto = produto
    
    __tablename__ = "itens_pedido"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)
    pedido = relationship("Pedido", back_populates="itens")
    produto = relationship("Produto")
    
    
    def setTotalPedidos (self, pedido, quantidade)-> int:
        def soma ():
            return self.__pedido * quantidade
        return soma
    
    def getTotalPedidos (self)->int:
        soma = self.setTotalPedidos(pedido, quantidade)
        return f'Total de pedios: {soma()}'
    
    
    def setdevolucao(self, quantidade, qtd_devolvida, produto_id)->int:
        devolucao = self.quantidade - qtd_devolvida
        prod = self.__produto_id
        
    def getdevolucao(self)->int:
        return f"DEvolveu-se: {self.quantidade - qtd_devolvida} do {self.produto_id}"
    
        


# %%
