import pandas as pd
import numpy as np


def summarize(df):

    #df = df.groupby(['city']).aggregate({'score': 'mean'}).reset_index()
    df = df.groupby(['city']).aggregate({'score': 'sum'}).reset_index()

    return df


city = ['BOS','BOS','BOS','NYC','NYC','NYC','CHI','CHI','CHI']
score = [50, 95, 82, 70, 70, 72, 38, 98, 55]

df = pd.DataFrame(zip(city, score), columns = ['city','score'])

df_sum = summarize(df)

print('summary df: ', df_sum)