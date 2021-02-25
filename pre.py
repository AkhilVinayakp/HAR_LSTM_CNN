"""
Created on Thu Feb 18 16:44:15 2021

@author: HP
"""

'''
preprocessing 
'''
import logging 
from main import *


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
data = HAR_PRE()
print(data.df.head())
data.full_info(chart=True)
data.save()