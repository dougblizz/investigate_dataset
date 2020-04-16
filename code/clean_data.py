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
    
#Dataframe with director
df_director = funct.clean_columns_with_pipeline(df_movies, 'director')

# Directores con mas peliculas con matplotlib
# plt.subplots(figsize = (16,12))
# df_director.director.value_counts().head().plot(kind = 'bar', label = 'movies per director')\
#                     .set_title('The 5 directors with the most films produced', fontsize = 20)
# plt.xlabel('directors', fontsize = 16)
# plt.ylabel('quantity', fontsize = 16)
# plt.legend(loc='upper right', fontsize = 16)
# plt.xticks(rotation = 360)

#Number of films per year.
plt.subplots(figsize = (16,12))
fig = sns.kdeplot(df_movies['release_year'], color = 'g', shade=True, label = 'movies')
plt.axvline(df_movies['release_year'].max(), linestyle='--', color='k', label='Threshold')
plt.legend(title=None, loc='upper right')

# Directores con mas peliculas con seaborn
plt.subplots(figsize = (16,12))
yo = df_director.director.value_counts().head()
yo = yo.to_frame()
yo.reset_index(level=0, inplace=True)
yo.rename(columns={'director': 'quantity'}, inplace=True)
yo.rename(columns={'index': 'director'}, inplace=True)
sns.barplot(x="director", y="quantity", data=yo).set_title('The 5 directors with the most films produced', fontsize = 20)


# Directores populares
au = df_director.director.value_counts() >= 10
au = au.to_frame() 
au.reset_index(level=0, inplace=True)
au.rename(columns={'index': 'dir'}, inplace=True)
au = au.dir[au['director'] == True]


real = df_director[df_director['director'].isin(au)]

x = real.groupby('director')['popularity'].max()
x.sort_values(ascending = False, inplace = True)
x = x.to_frame()
x.reset_index(level=0, inplace=True)

plt.subplots(figsize = (16,12))
sns.barplot(x="director", y="popularity", data=x.head(),  palette="Blues_d")


#Which genres are most popular from year to year? (Probando)
frames = []
cont = 1960
while(True):
    if cont <= 2010:
        frames.append(df_genres[df_genres['release_year'] == cont].groupby('genres')[['release_year','popularity']].max().head())
    else:
        frames.append(df_genres[df_genres['release_year'] == 2015].groupby('genres')[['release_year','popularity']].max().head())
        break
    cont += 10

result = pd.concat(frames)
result.reset_index(level=0, inplace=True)

plt.subplots(figsize = (20,18))
sns.barplot(x = "release_year", y = "popularity", hue = 'genres', data=result).set_title(f'Most popular genres', fontsize = 20)

#What kinds of propertiesare associated with movies that have high revenues?
#Headmap
f,ax = plt.subplots(figsize = (18,14))
sns.heatmap(df_movies.corr(), annot = True, linewidths=.5, fmt = '.1f', ax = ax)

# Revenue vs Budget
plt.subplots(figsize = (14,12))
splot = sns.scatterplot(x='revenue', y='budget', hue ='release_year', size = 'release_year', alpha = 0.5, sizes = (20,300), data=df_movies)
# splot.set(xscale="log")
# splot.set(yscale="log")

# Revenue vs vote_count
plt.subplots(figsize = (14,12))
sns.scatterplot(x='revenue', y='vote_count', hue ='release_year', size = 'release_year', alpha = 0.5, sizes = (20,300), data=df_movies)

# Revenue vs vote_count
plt.subplots(figsize = (14,12))
sns.scatterplot(x='revenue', y='popularity', hue ='release_year', size = 'release_year', alpha = 0.5, sizes = (20,300), data=df_movies)




# sns.regplot(x = 'revenue', y = 'popularity', ci = 100, data = df_movies)

# boxplot
# plt.subplots(figsize = (20,16))
# sns.boxplot(x = 'genres', y = 'popularity', data = df_genres[df_genres['release_year'] == 2010])

# f,ax = plt.subplots(figsize = (18,14))
# sns.heatmap(df_aux.corr(), annot = True, linewidths=.5, fmt = '.1f', ax = ax)
# plt.show()

# df_aux[df_aux['release_year'] == 2015].groupby('genres')['release_year'].count().plot(kind = 'bar')

# scatter_matrix(values, alpha=0.2, figsize=(18, 18))
