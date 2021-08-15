import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#reading the csv file
df = pd.read_csv('AdmissionPredict.csv')

#printing the info about csv data
print(df.describe())
print(df.info())

#gettinig rid of null taget(Chance of Admit)
df = df.drop(['Serial No.'],axis=1)

df = df.dropna(subset=['Chance of Admit'])


df['CGPA'] = df['CGPA'].replace(np.nan, df['CGPA'].mean())
df['GRE Score'] = df['GRE Score'].replace(np.nan, df['GRE Score'].mean())
df['TOEFL Score'] = df['TOEFL Score'].replace(np.nan, df['TOEFL Score'].mean())
# alternative method is to use mode