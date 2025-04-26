
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
  - `SQLite (o banco será criado automaticamente)`
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
   - O sistema utiliza modelos SQLAlchemy para representar as tabelas `Produto`, `Cliente`, `Pedido` e `ItemPedido`. Abaixo está a estrutura de cada tabela:

### **Produto**
Armazena informações sobre os produtos.

| Campo        | Tipo         | Descrição                       |
|--------------|--------------|---------------------------------|
| `id`         | `INTEGER`    | ID único do produto             |
| `nome`       | `VARCHAR`    | Nome do produto                 |
| `categoria`  | `VARCHAR`    | Categoria do produto            |
| `preco`      | `FLOAT`      | Preço do produto                |

### **Cliente**
Armazena informações sobre os clientes.

| Campo         | Tipo        | Descrição                             |
|---------------|-------------|---------------------------------------|
| `id`          | `INTEGER`   | ID único do cliente                   |
| `nome`        | `VARCHAR`   | Nome do cliente                       |
| `endereco`    | `VARCHAR`   | Endereço do cliente                   |
| `telefone`    | `VARCHAR`   | Telefone do cliente                   |
| `status`      | `VARCHAR`   | Status do cliente (Ex: "Ativo", "Inativo") |
| `limite_credito` | `FLOAT`   | Limite de crédito do cliente (calculado com base no status) |

### **Pedido**
Armazena informações sobre os pedidos realizados pelos clientes.

| Campo       | Tipo        | Descrição                               |
|-------------|-------------|-----------------------------------------|
| `id`        | `INTEGER`   | ID único do pedido                      |
| `cliente_id`| `INTEGER`   | ID do cliente (chave estrangeira)       |
| `data`      | `DATE`      | Data do pedido                          |

### **ItemPedido**
Armazena os itens de cada pedido, incluindo a quantidade de produtos e o produto associado.

| Campo       | Tipo        | Descrição                               |
|-------------|-------------|-----------------------------------------|
| `id`        | `INTEGER`   | ID único do item do pedido              |
| `pedido_id` | `INTEGER`   | ID do pedido (chave estrangeira)        |
| `produto_id`| `INTEGER`   | ID do produto (chave estrangeira)       |
| `quantidade`| `INTEGER`   | Quantidade do produto no pedido         |

