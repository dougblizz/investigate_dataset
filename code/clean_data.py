#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dougblizz
"""

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import funct

plt.style.use('ggplot')


df = pd.read_csv('../dataset/tmdb-movies.csv')

# Create df_ movies
df_movies = df[['popularity', 'budget', 'revenue', 'original_title', 'cast', 'director', 'runtime', 'genres', 
                'production_companies', 'release_date','vote_count', 'vote_average', 'release_year', 'budget_adj', 'revenue_adj']]

# Remove unnecessary rows
df_movies = df_movies[(df_movies['budget'] != 0) & (df_movies['revenue'] != 0)]

# Drop na values
df_movies.dropna(inplace = True)

# Dataframe without outliers
Q1 = df_movies.quantile(0.25)
Q3 = df_movies.quantile(0.75)
IQR = Q3 - Q1
df_without_outliers = df_movies[((df_movies < (Q1 - 1.5 * IQR)) | (df_movies > (Q3 + 1.5 * IQR))).any(axis=1)]

# Dataframe with genres
df_genres = funct.clean_columns_with_pipeline(df_without_outliers, 'genres')

# Dataframe with cast
df_cast = funct.clean_columns_with_pipeline(df_without_outliers, 'cast')

# Dataframe with production_companies
df_production = funct.clean_columns_with_pipeline(df_without_outliers, 'production_companies')
    
# Dataframe with director
df_director = funct.clean_columns_with_pipeline(df_without_outliers, 'director')


# Number of films per year.
plt.subplots(figsize = (16,12))
fig = sns.kdeplot(df_movies['release_year'],\
                  color = 'g',\
                  shade = True,\
                  label = 'movies')\
                  .set_title('Number of films per year',\
                       fontsize = 20)

plt.axvline(df_movies['release_year'].max(), linestyle = '--', color = 'k', label = 'Threshold')
plt.legend(loc='upper right')


# Which genres are most popular from years
frames = []
cont = 1960
while(True):
    if cont <= 2010:
        aux = df_genres[df_genres['release_year'] == cont].groupby('genres')['popularity'].mean()
        aux = aux.to_frame()
        aux.reset_index(level=0, inplace=True)
        aux['year'] = cont
        aux.sort_values(by = 'popularity', ascending = False)
        frames.append(aux.head())
    else:
        aux = df_genres[df_genres['release_year'] == 2015].groupby('genres')['popularity'].mean()
        aux = aux.to_frame()
        aux.reset_index(level=0, inplace=True)
        aux['year'] = 2015
        aux.sort_values(by = 'popularity', ascending = False)
        frames.append(aux.head())
        break
    cont += 10

new_genres = pd.concat(frames)
new_genres.reset_index(level=0, inplace=True)

plt.subplots(figsize = (16,12))
sns.barplot(x = "year",
            y = "popularity",\
            hue = 'genres',\
            data = new_genres)\
            .set_title('Most popular genres', fontsize = 20)


    
# What kinds of properties are associated with movies that have high revenues?

# Headmap with correlation
f,ax = plt.subplots(figsize = (18,14))
sns.heatmap(df_movies.corr(),\
            annot = True,\
            linewidths=.5,\
            fmt = '.1f',\
            ax = ax)


# Revenue vs Budget
funct.plot_scatter(df_movies, 'revenue', 'budget', 'release_year')

# Revenue vs vote_count
funct.plot_scatter(df_movies, 'revenue', 'vote_count', 'release_year')
    
# Revenue vs popularity
funct.plot_scatter(df_movies, 'revenue', 'popularity', 'release_year')

# Director min value (Subjective)
df_director.director.value_counts().head(20)

# Directors with more movies
funct.quantity(df_director, 'director')

# Most popular directors
funct.popular(df_director, 'director', 9)
    
# Most revenue directors
funct.revenue(df_director, 'director', 9)

# Directors with high budget
funct.budget(df_director, 'director', 9)

# Actors min value (Subjective)
df_cast.cast.value_counts().head(20)

# Actors with more movies
funct.quantity(df_cast, 'cast')

# Most popular actors
funct.popular(df_cast, 'cast', 10)

# Most revenue actors
funct.revenue(df_cast, 'cast', 10)

# Actors with high budget
funct.budget(df_cast, 'cast', 10)

# production_companies min value (Subjective)
df_production.production_companies.value_counts().head(20)

# production_companies with more movies
funct.quantity(df_production, 'production_companies')

# Most popular production_companies
funct.popular(df_production, 'production_companies', 10)

# Most revenue production_companies
funct.revenue(df_production, 'production_companies', 10)

# Most revenue genres
funct.budget(df_production, 'production_companies', 10)

# genres min value (Subjective)
df_genres.genres.value_counts().min()

# genres with more movies
funct.quantity(df_genres, 'genres')

# Most popular genres
funct.popular(df_genres, 'genres', df_genres.genres.value_counts().min())

# Most revenue genres
funct.revenue(df_genres, 'genres', df_genres.genres.value_counts().min())

# Most budget genres
funct.budget(df_genres, 'genres', df_genres.genres.value_counts().min())