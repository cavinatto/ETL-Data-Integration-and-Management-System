
# Sistema de Integração e Gerenciamento de Dados (ETL)

Este projeto implementa um processo ETL (Extração, Transformação e Carga) que integra dados de um arquivo Excel em um banco de dados SQL, além de gerenciar informações relacionadas a clientes, produtos, pedidos e itens de pedidos. O sistema extrai dados de um arquivo Excel, transforma esses dados para o formato adequado de banco de dados e carrega-os em tabelas relacionadas. O projeto também inclui modelos de dados representando clientes, produtos, pedidos e itens de pedidos, com funcionalidades como cálculo de limites de crédito baseado no status do cliente.

---

## **Visão Geral do Projeto**

- **Processo ETL**: Extrai dados de um arquivo Excel, transforma-os para o formato de banco de dados e carrega-os no banco.
- **Modelos de Dados**: Representações de clientes, produtos, pedidos e itens de pedidos.
- **Migrações**: Gerenciamento de alterações no esquema do banco usando Alembic.

---

## **Requisitos**

- Python 3.x
- Dependências:
  - `pandas`, `sqlalchemy`, `pyodbc`, `alembic`, `dotenv`, `openpyxl`
- Banco de Dados:
  - `SQLite`
---

## **Instalação**

1. Clone o repositório:

```bash
git clone https://github.com/cavinatto/Excel2DB
cd Excel2DB
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## **Configuração**

1. **Configuração do Banco de Dados**:
   - Crie um arquivo `.env` com as credenciais do banco.

2. **Migrações**:
   - Para aplicar migrações:

```bash
alembic upgrade head
```

---

## **Como Usar**

1. **Executando o ETL**:
   - Edite o arquivo `etl.py` para configurar a URL de conexão do banco e o caminho do arquivo Excel.
   - Execute o ETL:

```python
from etl import ETL

etl = ETL(db_url="seu_banco_de_dados", file_path="caminho/para/excel")
etl.run()
```

2. **Modelos de Dados**:
   - O sistema utiliza modelos SQLAlchemy para representar as tabelas `Produto`, `Cliente`, `Pedido` e `ItemPedido`. Mais detalhes estão disponíveis no arquivo `models.py`.

