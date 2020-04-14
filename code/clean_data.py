#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dougblizz
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns;
import funct

plt.style.use('ggplot')


df = pd.read_csv('../dataset/tmdb-movies.csv')

#Create df_ movies
df_movies = df[['popularity', 'budget', 'revenue', 'original_title', 'cast', 'director', 'runtime', 'genres', 
                'production_companies', 'release_date','vote_count', 'vote_average', 'release_year', 'budget_adj', 'revenue_adj']]

#Remove unnecessary rows
df_movies = df_movies[(df_movies['budget'] != 0) & (df_movies['revenue'] != 0)]

#Drop na values
df_movies.dropna(inplace = True)

# Dataframe with genres
df_genres = funct.clean_columns_with_pipeline(df_movies, 'genres')

# Dataframe with cast
df_cast = funct.clean_columns_with_pipeline(df_movies, 'cast')

#Dataframe with production_companies
df_production = funct.clean_columns_with_pipeline(df_movies, 'production_companies')
    




#x = df_clean_cast.groupby('genres')['cast'].nunique()


#Number of movies per year
# plt.subplots(figsize = (20,16))
# fig = sns.kdeplot(df_movies['release_year'], color = 'g', shade=True, label = 'movies')
# plt.axvline(df_movies['release_year'].max(), linestyle='--', color='k', label='Threshold')
# plt.legend(title=None, loc='upper right')

# # boxplot
# plt.subplots(figsize = (20,16))
# sns.boxplot(y = 'budget', x = 'release_year',  data = values[values['release_year'] >= 2010])

# df_movies[df_movies['release_year'] == 2015].count()






# f,ax = plt.subplots(figsize = (18,14))
# sns.heatmap(df_aux.corr(), annot = True, linewidths=.5, fmt = '.1f', ax = ax)
# plt.show()


# df_aux[df_aux['release_year'] == 2015].groupby('genres')['release_year'].count().plot(kind = 'bar')

# scatter_matrix(values, alpha=0.2, figsize=(18, 18))

# plt.figure( figsize = (12,10))
# sns.scatterplot(x = 'revenue', y = 'budget', size="release_year", hue="release_year", data = df_movies)

# sns.regplot(x = df_aux['revenue'], y = df_aux['vote_count'])