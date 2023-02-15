import os
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from sqlalchemy.pool import QueuePool
load_dotenv()
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus

DB_DRIVER = os.getenv('DBDRIVER')
SCHEMA = os.getenv('SCHEMA')
POOL_SIZE = os.getenv('POOL_SIZE')
DB_USER = os.getenv('DBUSER')
DB_PASS = os.getenv('DBPASS')
DB_HOST = os.getenv('DBHOST')
PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DBNAME')

DATABASE_URL = f"{DB_DRIVER}{DB_USER}:{quote_plus(DB_PASS)}@{DB_HOST}:{PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, poolclass=QueuePool, pool_size=int(POOL_SIZE), max_overflow=20,
                       connect_args={'options': '-csearch_path={}'.format(str(SCHEMA))}, echo=False)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

''' --------------- DOC--------------
The above code is a Python script that creates a connection to a SQL database using
the SQLAlchemy library.

It first imports several required modules such as os, 
SQLAlchemy's declarative_base, dotenv, sqlalchemy's QueuePool 
and sessionmaker, and urllib's quote_plus. It also calls the 
dotenv.load_dotenv() function to load environment variables from a .env file.

Next, it retrieves various database connection details from environment variables such 
as DBDRIVER, SCHEMA, POOL_SIZE, DBUSER, DBPASS, DBHOST, DB_PORT, and DBNAME. 
It then constructs the database URL string using these details and creates a 
SQLAlchemy engine with create_engine() function. The engine is configured with a
 QueuePool and connection arguments to set the schema search path.
 
Finally, it defines a session maker using sessionmaker() and sets it 
to bind to the previously created engine. It also creates a declarative 
base using declarative_base() function from SQLAlchemy.
'''