# ETL-Data-Integration-and-Management-System

This project implements an ETL (Extract, Transform, Load) process that integrates data from an Excel file into a SQL database, as well as manages information related to customers, products, orders, and order items. The system extracts data from an Excel file, transforms the data into the proper format for a database, and loads it into related tables. The project also includes data models representing customers, products, orders, and order items, with the ability to perform operations like calculating credit limits based on customer status.

---

## **Table of Contents**

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Environment Configuration](#environment-configuration)
- [How to Use](#how-to-use)
  - [Running Migrations](#running-migrations)
  - [Running the ETL](#running-the-etl)
  - [Data Models](#data-models)

---

## **Project Overview**

The system consists of the following main parts:

1. **ETL Process**: Extracts data from an Excel file, transforms it to match the database format, and loads it into the database.
2. **Models**: SQLAlchemy models representing `Produto`, `Cliente`, `Pedido`, `ItemPedido`, and `StatusCliente`.
3. **Migration with Alembic**: Migrations are used to manage database schema changes.

---

## **Requirements**

- Python 3.x
- Dependencies:
  - `pandas`
  - `sqlalchemy`
  - `pyodbc`
  - `alembic`
  - `dotenv`
  - `openpyxl` (for reading Excel files)

---

## **Installation**

1. Clone this repository to your local machine:

```bash
git clone https://github.com/cavinatto/ETL-Data-Integration-and-Management-System
cd ETL-Data-Integration-and-Management-System
```
2. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

### 1. Create the .env file

Create a `.env` file in the root of the project with the following database credentials:

```ini
USUARIO=your_username
SENHA=your_password
HOST=your_host
BANCO_DE_DADOS=your_database
```

### 2. Database Configuration

The project is set up to use SQLAlchemy to interact with a database. The connection URL is configured in `env.py` using the database credentials specified in the `.env` file.

---

## How to Use

### 1. Running Migrations

To run migrations and apply the database schema changes, use Alembic. You can apply the latest migration with:

```bash
alembic upgrade head
```
This will update the database schema to match the latest migration.

---

### 2. Running the ETL

The `etl.py` file contains the ETL class, which is responsible for extracting data from an Excel file, transforming the data, and loading it into the database.

To run the ETL process:

1. Define the database connection URL and the path to your Excel file in `etl.py`.

```python
from etl import ETL

# Define the connection parameters
db_url = "sqlite:///banco_de_dados.db"  # Database URL
file_path = "dados_iniciais.xlsx"       # Excel file path

etl = ETL(db_url=db_url, file_path=file_path)
extracted_data = etl.extract()
transformed_data = etl.transform(extracted_data)
etl.load(transformed_data)
```
The ETL will extract the data from the Excel file, transform it into the correct format, and load it into the database.

---

### 3. Data Models

The data models represent the following tables:

- **Produto**: Stores product information (id, nome, categoria, preco).
- **Cliente**: Stores customer information, including their credit limit, which is influenced by their status (id, nome, endereco, telefone, status, limite_credito).
- **Pedido**: Stores order information, each associated with a customer (id, cliente_id, data).
- **ItemPedido**: Stores items in each order, including quantity and associated product (id, pedido_id, produto_id, quantidade).

Each model is represented as a SQLAlchemy class and is mapped to a table in the database.

---
