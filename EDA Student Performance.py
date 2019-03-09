# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('StudentsPerformance.csv')
x = dataset.iloc[:,:-3].values
y = dataset.iloc[:,5:].values


# Adding Total Marks Column

dataset['Total Marks'] = dataset['math score'] + dataset['reading score'] + dataset['writing score']

# information on dataset

dataset.info()

# Mean score  in math, reading and writing based on gender
x1 = dataset.groupby('gender')['math score'].mean()
x2 = dataset.groupby('gender')['reading score'].mean()
x3 = dataset.groupby('gender')['writing score'].mean()
x4 = dataset.groupby('gender')['Total Marks'].mean()

# combining the mean values for math, reading and writing

x_mean = pd.concat([x1,x2,x3], axis=1)


# Mean score  in math, reading and writing based on race/ethnicity

xm = dataset.groupby('race/ethnicity')['math score'].mean()
xr = dataset.groupby('race/ethnicity')['reading score'].mean()
xw = dataset.groupby('race/ethnicity')['writing score'].mean()
xt = dataset.groupby('race/ethnicity')['Total Marks'].mean()

xe_mean = pd.concat([xm,xr,xw,xt], axis =1)

# Mean score  in math, reading and writing based on parental level of education

xpm = dataset.groupby('parental level of education')['math score'].mean()
xpr = dataset.groupby('parental level of education')['reading score'].mean()
xpw = dataset.groupby('parental level of education')['writing score'].mean()
xpt = dataset.groupby('parental level of education')['Total Marks'].mean()

xp_mean = pd.concat([xpm,xpr,xpw,xpt], axis =1)

# Mean score  in math, reading and writing based on Lunch

xlm = dataset.groupby('lunch')['math score'].mean()
xlr = dataset.groupby('lunch')['reading score'].mean()
xlw = dataset.groupby('lunch')['writing score'].mean()
xlt = dataset.groupby('lunch')['Total Marks'].mean()

xl_mean = pd.concat([xlm,xlr,xlw,xlt], axis =1)

# Mean score  in math, reading and writing based on test preparation course
xtm = dataset.groupby('test preparation course')['math score'].mean()
xtr = dataset.groupby('test preparation course')['reading score'].mean()
xtw = dataset.groupby('test preparation course')['writing score'].mean()
x4t = dataset.groupby('test preparation course')['Total Marks'].mean()

xt_mean = pd.concat([xtm,xtr,xtw,x4t], axis =1)




