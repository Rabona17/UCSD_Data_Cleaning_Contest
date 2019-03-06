import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer

class CleanerMonthly:
    """
    This class is for fill nan values of a column 
    using the mean value of a certain month of that column.
    For instance, to fillna for temperature in 2001-11-01 at wsnm a,
    we use the mean temp at November at wsnm a.
    """
    imputer = Imputer(missing_values = 0, strategy = 'mean', axis = 0)
    def __init__(self, dataframe):
        self.df = dataframe
        self.filled_column = np.empty((1,31))
        
    def cleaning_monthly(self, column_index, staring, end, key = 'wsnm'):
        cities_updated = self.df.groupby(key)
        city_list_updated = np.array(list(cities_updated.groups.keys()))
        for city in city_list_updated[staring:end]:
            date_list = cities_updated.get_group(city).groupby('mo').groups.keys()
            for date in date_list:
                single = cities_updated.get_group(city).groupby('mo').get_group(date).iloc[:, :].values
                try:
                    single[:, column_index] = self.imputer.fit_transform(single[:, column_index].reshape(-1,1)).reshape(1,-1)[0]
                except ValueError:
                    single[:, column_index] = np.empty(len(single))
                self.filled_column = np.concatenate((self.filled_column, single))
            print(city)        
