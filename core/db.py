from sqlalchemy import create_engine, MetaData, Table, inspect
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker

DATABASE_URL= ""

engine = create_engine(DATABASE_URL, echo=False)

metadata = MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def reflect_single_table(table_name):
    try:
        table = Table(table_name, metadata, autoload_with=engine, extend_existing=True)
        return table
    except Exception as e:
        print(f"Error reflejando tabla '{table_name}': {e}")
        return None
    
