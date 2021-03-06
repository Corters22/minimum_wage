# dependencies
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, join, outerjoin, MetaData, Table

from clean_data import connection_string

class MinimumWage():

    def __init__(self):
        self.engine = create_engine(connect_string)
        # self.conn = self.engine.connect()
        self.connect_string = connect_string
        self.inspector = inspect(self.engine)
        self.tables = self.inspector.get_table_names()
        self.Base = automap_base()
        self.Base.prepare(self.engine, reflect=True)
        self.Subjects = self.Base.classes['subjects']
        self.meta = MetaData()
        self.TestResults = Table('test_results_view', self.meta, 
                    autoload_with=self.engine)
    
    def display_db_info(self):
        inspector = inspect(self.engine)
        tables = self.inspector.get_table_names()
        for table in self.tables:
            print("\n")
            print('-' * 12)
            print(f"table '{table}' has the following columns:")
            print('-' * 12)
            for column in self.inspector.get_columns(table):
                print(f"name: {column['name']}   column type: {column['type']}")

    def states_list(self):
        session = Session(self.engine)

        results = session.query(self.min_wage.State)
            
        df = pd.read_sql(results.statement, session.connection())

        session.close()  
        return list(df.State) 

    def get_min_wage(self):
        session=Session(self.engine)

        if chosen_state='United States':
            results=Session.query(self.min_wage)
        else:
            results=Session.query(self.min_wage).filter(self.min_wage.State == chosen_state)
        df = pd.read_sql(results.statement, session.connection())
        return df.to_dict(orient='records')
    
    def get_education(self):
        session=Session(self.engine)

        results=Session.query(self.educ_level).filter(self.educ_level.Area_name == chosen_state)
        df= pd.read_sql(results.statement, session.connection())
        return df.to_dict(orient='records')
    
    