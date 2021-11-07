import pandas as p
import csv 
import plotly.figure_factory as pff

df  = p.read_csv('brand-rating.csv')
fig = pff.create_distplot(
    [df['Avg Rating']],
    ['name']
)
fig.show()