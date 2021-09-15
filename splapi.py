import pandas as pd
from sodapy import Socrata

class checkout_titles:
    def __init__(self, limit=1000, datasource= "data.seattle.gov", ID="tmmm-ytt6", results_df=None):
        
        '''Default to calling the Seattle Public Library Checkouts by title dataset. Other datasets can be called if specified initially.'''
    
        self.limit = limit
        self.datasource = datasource
        self.ID = ID
        self.results_df= results_df
        
    def load_subset(self, limit=1000, query=False):
        '''Uses the sodapy Socrata as an API to access the Seattle Public Library checkouts dataset.'''
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
            results = client.get(self.ID, limit=limit)
            self.results_df = pd.DataFrame.from_records(results)
            
        return self.results_df.head()

    def save_subset(self, filepath, update=False):
        '''Saves the subset of data loaded from the Seattle Public Library Checkouts dataset as csv.'''
        
        if update:
            self.update_df.to_csv(filepath)
            
        else:
            self.results_df.to_csv(filepath)
                                 
    def update_dataset(self, filepaths=[]):
        '''This function concatenates a previous subset or subsets of data into one dataframe called update_df. The filepaths variable is a list of CSV filepaths that the user wants concatenated. Each CSV file is then loaded into a pandas dataframe, and those dataframes are then combined on the row. Note filepaths must be a list with at least 2 elements for the function to work.'''

        df_list = [pd.read_csv(file) for file in filepaths]
        self.update_df = pd.concat(df_list)
        
        return self.update_df.head()
