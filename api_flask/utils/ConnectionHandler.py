from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

class ConnectionHandler():

    @classmethod
    def get_engine(cls):

        return create_engine(f'mssql+pyodbc://GUSTAVO\SQLEXPRESS/MY_LIB_FILMES?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')