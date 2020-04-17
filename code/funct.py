#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dougblizz
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

def clean_columns_with_pipeline(df, column):
    
    df_aux = pd.DataFrame(df[column].str.split('|'))
    aux_series = df_aux[column].apply(pd.Series).stack().reset_index(1)
    aux_series.drop('level_1', axis = 1, inplace = True)
    final_df = df.join(aux_series)
    final_df.drop(column, axis = 1, inplace = True)
    final_df.rename(columns={0:column}, inplace=True)
    return final_df

def plot_scatter(df, col1, col2, year):
    plt.subplots(figsize = (14,12))
    sns.scatterplot(x = col1,\
                    y = col2,\
                    hue = year,\
                    size = year,\
                    alpha = 0.5,\
                    sizes = (20,300),\
                    data = df)
        
def quantity(df, col):
    
    plt.subplots(figsize = (16,12))
    df_aux = df[col].value_counts().head()
    df_aux = df_aux.to_frame()
    df_aux.reset_index(level = 0, inplace = True)
    df_aux.rename(columns = {col: 'quantity'}, inplace = True)
    df_aux.rename(columns = {'index': col}, inplace = True)
    
    title = ''
    if col == 'director':
        title = 'Directors with the most films produced'
    elif col == 'cast':
        title = 'Actors with the most films appearances'
    elif col == 'genres':
        title = 'Genres with more movies'
    else:
        title = 'Companies with most films produced'
        
    sns.barplot(x = col,\
                y = "quantity",\
                data = df_aux)\
                .set_title(title,\
                           fontsize = 20)

def popular(df, col, min_value):
    df_aux = df[col].value_counts() >= min_value
    df_aux = df_aux.to_frame() 
    df_aux.reset_index(level=0, inplace=True)
    df_aux.rename(columns={'index': 'name'}, inplace=True)
    df_aux = df_aux.name[df_aux[col] == True]
    
    df_aux = df[df[col].isin(df_aux)]
    
    df_aux = df_aux.groupby(col)['popularity'].mean()
    df_aux.sort_values(ascending = False, inplace = True)
    df_aux = df_aux.to_frame()
    df_aux.reset_index(level=0, inplace=True)
    
    title = ''
    if col == 'director':
        title = 'Most popular directors'
    elif col == 'cast':
        title = 'Most popular actors'
    elif col == 'genres':
        title = 'Most popular genres'
    else:
        title = 'Most popular companies'
    
    plt.subplots(figsize = (16,12))
    sns.barplot(x=col, y="popularity", data = df_aux.head(),  palette="Reds_d")\
                .set_title(title, fontsize = 20)
                
def revenue(df, col, min_value):
    df_aux = df[col].value_counts() >= min_value
    df_aux = df_aux.to_frame() 
    df_aux.reset_index(level=0, inplace=True)
    df_aux.rename(columns={'index': 'name'}, inplace=True)
    df_aux = df_aux.name[df_aux[col] == True]
    
    df_aux = df[df[col].isin(df_aux)]
    
    df_aux = df_aux.groupby(col)['revenue'].mean()
    df_aux.sort_values(ascending = False, inplace = True)
    df_aux = df_aux.to_frame()
    df_aux.reset_index(level=0, inplace=True)
    
    title = ''
    if col == 'director':
        title = 'Most revenue directors'
    elif col == 'cast':
        title = 'Most revenue actors'
    elif col == 'genres':
        title = 'Most revenue genres'
    else:
        title = 'Most revenue companies'
    
    plt.subplots(figsize = (16,12))
    sns.barplot(x=col, y="revenue", data = df_aux.head(),  palette="Blues_d")\
                .set_title(title, fontsize = 20)
 

def budget(df, col, min_value):
    df_aux = df[col].value_counts() >= min_value
    df_aux = df_aux.to_frame() 
    df_aux.reset_index(level=0, inplace=True)
    df_aux.rename(columns={'index': 'name'}, inplace=True)
    df_aux = df_aux.name[df_aux[col] == True]
    
    df_aux = df[df[col].isin(df_aux)]
    
    df_aux = df_aux.groupby(col)['budget'].mean()
    df_aux.sort_values(ascending = False, inplace = True)
    df_aux = df_aux.to_frame()
    df_aux.reset_index(level=0, inplace=True)
    
    title = ''
    if col == 'director':
        title = 'Directors with high budget'
    elif col == 'cast':
        title = 'Actors with high budget'
    elif col == 'genres':
        title = 'Genres with more budget'
    else:
        title = 'Companies with high budget'
    
    plt.subplots(figsize = (16,12))
    sns.barplot(x=col, y="budget", data = df_aux.head(),  palette="Purples_d")\
                .set_title(title, fontsize = 20)