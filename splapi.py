import pandas as pd
from sodapy import Socrata
from sqlalchemy import create_engine
class checkout_titles:
    def __init__(self, limit=1000, datasource="data.seattle.gov", ID="tmmm-ytt6", results_df=None):
        '''Default to call the Seattle Public Library Checkouts
        dataset, but it can call other databases via socrata.'''
        self.limit = limit
        self.datasource = datasource
        self.ID = ID
        self.results_df= results_df
    def load_subset(self, limit, query=False):
        '''Uses the sodapy Socrata as an API to access the 
            Seattle Public Library checkouts dataset.'''
        client = Socrata(self.datasource, None)
        if query is not False:
            try:
                results = client.get(self.ID, query=query)
            except HTTPError:
                print('For queries, terms, such as select, groupby, or where,',
                      'need to be lowercase. Strings need to be in quotes',
                      'e.g. "EBOOK" and numbers need to not have quotes.')
            self.results_df = pd.DataFrame.from_records(results)
        else:
            results = client.get("tmmm-ytt6", limit=limit)
            self.results_df = pd.DataFrame.from_records(results)
        return self.results_df.head()
    
    def save_subset(self, table_name, db = local=False, update=False):
        '''Saves the queried subset of data loaded from the Seattle Public Library Checkouts dataset either localy as a CSV or to a SQL database. The default is a database.''' 
        if local:
            self.results_df.to_csv(table_name)
            if update:
                self.update_df.to_csv(table_name)
        else:                
            engine = create_engine('sqlite:///SeattleLibraryCheckouts.db')
            if update:
                self.update_df.to_sql(table_name, con = engine, if_exists='append', index=False)
            else:
                self.results_df.to_sql(table_name, con = engine, if_exists='fail', index=False)
        
    def update_dataset(self, filepaths=[]):
        '''This function concatenates a previous subset or subsets of data into one dataframe 
        called update_df. The filepaths variable is a list of CSV filepaths that the user wants concatenated.
        Each CSV file is then loaded into a pandas dataframe, and those dataframes are then appended.
        
        Note filepaths must be a list with at least 2 elements for the function to work.'''
        
        df_list = [pd.read_csv(file) for file in filepaths]
        self.update_df = pd.concat(df_list)
        return self.update_df.head()
            
