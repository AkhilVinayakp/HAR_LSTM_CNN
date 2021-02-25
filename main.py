"""
The main class of HAR processing
cleaning data wisdm
"""
"""
|||importing modules
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import logging

from pandas.core.frame import DataFrame

# setting up basic config for logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


class HAR_PRE:
    def __init__(self) -> None:
        """loading the dataset"""
        columns = ['user','activity','timestamp', 'x-axis', 'y-axis', 'z-axis']
        self.df = pd.read_csv('data/WISDM_raw.txt', header = None, names = columns)
        self.pre()
    def pre(self):
        ''' the  last column contains a ; at the end of each value removing it'''
        self.df['z-axis'].replace(regex=True, inplace=True, to_replace=r';', value=r'')
        logging.debug([type(self.df[i][0]) for i in self.df.columns])
        # changing the last axis value to float64
        self.df['z-axis'] = self.df['z-axis'].astype(np.float64)
        logging.debug([type(self.df[i][0]) for i in self.df.columns])
    def full_info(self, chart = False):
        print("\n INFO OF the DataSet")
        print(self.df.info())
        # print("\n Count of each class values>>>>>>>>>>>>")
        if chart:
            print("chart")
            self.df['activity'].value_counts().plot(kind = 'bar', title='activity vs count')
            plt.show()
            self.df['user'].value_counts().plot(kind = 'bar', title="user vs count")
            plt.show()
    def save(self):
        path = os.path.join(os.getcwd(),'data','wisdm_cln.csv')
        try:
            self.df.to_csv(path, index=False)
            logging.debug(f"successfully saved to {path}")
        except Exception as e:
            print("Operation Failed")
            print(f"\n {e}")



