#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dougblizz
"""


def clean_columns_with_pipeline(df, column):
    import pandas as pd 
    
    df_aux = pd.DataFrame(df[column].str.split('|'))
    aux_series = df_aux[column].apply(pd.Series).stack().reset_index(1)
    aux_series.drop('level_1', axis = 1, inplace = True)
    final_df = df.join(aux_series)
    final_df.drop(column, axis = 1, inplace = True)
    final_df.rename(columns={0:column}, inplace=True)
    return final_df
