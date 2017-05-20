import pandas as pd
from pandas import Series, DataFrame, Panel
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import requests
import matplotlib
matplotlib.style.use('ggplot')
def country_based_data(country_name,file,series):
    data2=file
    series_name=series
    infla_data1 = data2[data2["Series Name"] == series_name]
    country_data = infla_data1['Country Name'] == country_name
    infla_data1 = infla_data1[country_data]
    infla_data1 = infla_data1.drop(['Series Name', 'Country Name'], axis=1)
    row1 = infla_data1.iloc[0]
    row1 = row1.astype(float)
    row1.plot(kind='line', x='Year', y='Value')
    plt.title(country_name + " -" + series_name)
    plt.show()


data = pd.read_csv("world-bank.csv",encoding ='latin1',index_col = False)
data2 = data.drop(['Series Code', 'Country Code'], axis=1)
country= input("Enter the name of the country:")
key_metric = input("Please enter a key_metric Inflation,GDP or Population:")
if key_metric=="Inflation":
    series1= "Inflation, consumer prices (annual %)"
    e=country_based_data(country,data2,series1)
    series2= "Inflation, GDP deflator (annual %)"
    e=country_based_data(country,data2,series2)
elif key_metric=="GDP":
    series1= "GDP per capita (current US$)"
    e=country_based_data(country,data2,series1)
    series2= "GDP (current US$)"
    e=country_based_data(country,data2,series2)
    series3= "GDP growth (annual %)"
    e=country_based_data(country,data2,series3)
elif key_metric=="Population":
    #series1= "Population Total"
    #e=country_based_data(country,data2,series1)
    series2= "Population growth (annual %)"
    e=country_based_data(country,data2,series2)
else:
    print ("Unknown metric- " + str(key_metric))