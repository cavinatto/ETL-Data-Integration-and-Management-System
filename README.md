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
- [Contributing](#contributing)
- [License](#license)

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

## **Environment Configuration**

1. Create a .env file in the root of the project with the following database credentials:

```bash
USUARIO=your_username
SENHA=your_password
HOST=your_host
BANCO_DE_DADOS=your_database
```

