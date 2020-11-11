#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


def get_curriculum_data():
    '''
    This function will read the curriculum text data and convert it to a dataframe
    '''
    
    colnames=['date', 'time', 'page_viewed', 'user_id', 'cohort_id', 'ip']
    df = pd.read_csv('anonymized-curriculum-access.txt', sep=' ', header=None, names=colnames)
    return df

def get_cohort_data():
    '''
    This function converts the csv into a dataframe
    '''
    
    df = pd.read_csv('cohorts.csv', index_col=0)
    return df

def merge_data():
    '''
    This function will merge both dataframes into one dataframe
    '''
    df1 = get_curriculum_data()
    df2 = get_cohort_data()
    # merge these into one dataframe
    df1 = df1.merge(df2, how='outer', on='cohort_id')  
    return df1

