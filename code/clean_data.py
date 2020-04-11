# -*- coding: utf-8 -*-


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns


df_movies = pd.read_csv('../dataset/tmdb-movies.csv')

df_movies.drop(['imdb_id', 'homepage', 'production_companies', 'tagline', 'keywords', 'overview'], axis = 1, inplace = True)


df_movies.dropna(inplace = True)


df = pd.DataFrame(df_movies['genres'].str.split('|'))

aux = df['genres'].apply(pd.Series).stack().reset_index(1)
aux.drop('level_1', axis=1, inplace = True)

df_final = df_movies.join(aux)



# f,ax = plt.subplots(figsize = (18,14))
# sns.heatmap(df_movies.corr(), annot = True, linewidths=.5, fmt = '.1f', ax = ax)
# plt.show()