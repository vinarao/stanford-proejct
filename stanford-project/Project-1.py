import pandas as pd
from pandas import Series, DataFrame, Panel
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import requests
import matplotlib
matplotlib.style.use('ggplot')
def country_based_data(country_name,file,series1,series2):
    data2=file
    series_name=series1
    infla_data1 = data2[data2["Series Name"] == series_name]
    country_data = infla_data1['Country Name'] == country_name
    infla_data1 = infla_data1[country_data]
    infla_data1 = infla_data1.drop(['Series Name', 'Country Name'], axis=1)
    row1 = infla_data1.iloc[0]
    row1 = row1.astype(float)
    row1.plot(kind='line', x=series_name, y= series_name,color='#4C72B0',label=series_name)
    series_name = series2
    infla_data2 = data2[data2["Series Name"] == series_name]
    country_data = infla_data2['Country Name'] == country_name
    infla_data2 = infla_data2[country_data]
    infla_data2 = infla_data2.drop(['Series Name', 'Country Name'], axis=1)
    row2 = infla_data2.iloc[0]
    row2= row2.astype(float)
    row2.plot(kind='line', x=series_name, y= series_name, color='#55A868',label=series_name)
    plt.title("Development Indicators" + " -" + country_name)
    plt.xlabel('year')
    plt.ylabel('Percentage change')
    plt.legend(loc='best')
    plt.show()

def country_all_based_data(country_name,file,series1,series2,series3):
    data2=file
    series_name=series1
    infla_data1 = data2[data2["Series Name"] == series_name]
    country_data = infla_data1['Country Name'] == country_name
    infla_data1 = infla_data1[country_data]
    infla_data1 = infla_data1.drop(['Series Name', 'Country Name'], axis=1)
    row1 = infla_data1.iloc[0]
    row1 = row1.astype(float)
    row1.plot(kind='line', x='Year', y='Value', color="green", label=series_name)
    series_name = series2
    infla_data2 = data2[data2["Series Name"] == series_name]
    country_data = infla_data2['Country Name'] == country_name
    infla_data2 = infla_data2[country_data]
    infla_data2 = infla_data2.drop(['Series Name', 'Country Name'], axis=1)
    row2 = infla_data2.iloc[0]
    row2= row2.astype(float)
    row2.plot(kind='line', x='Year', y='Value', color= "black", label=series_name)
    series_name = series3
    infla_data3 = data2[data2["Series Name"] == series_name]
    country_data = infla_data3['Country Name'] == country_name
    infla_data3 = infla_data3[country_data]
    infla_data3 = infla_data3.drop(['Series Name', 'Country Name'], axis=1)
    row3 = infla_data3.iloc[0]
    row3= row3.astype(float)
    row3.plot(kind='line', x='Year', y='Value', color= "blue", label=series_name)
    plt.title("Development Indicators" + " -" + country_name )
    plt.legend(loc='best')
    plt.xlabel('year')
    plt.ylabel('Percentage change')
    plt.show()

data = pd.read_csv("world-bank.csv",encoding ='latin1',index_col = False)
data2 = data.drop(['Series Code', 'Country Code'], axis=1)
country= input("Enter the name of the country:")
key_metric = input("Please enter a key_metric Inflation,GDP or Population:")
if key_metric=="Inflation":
    series1= "Inflation, consumer prices (annual %)"
    series2= "Inflation, GDP deflator (annual %)"
    e=country_based_data(country,data2,series1,series2)
elif key_metric=="GDP":
    series1= "GDP per capita (current US$)"
    series2= "GDP growth (annual %)"
    e=country_based_data(country,data2,series1,series2)
elif key_metric=="Population":
    series1= "Population Total"
    series2= "Population growth (annual %)"
    e=country_based_data(country,data2,series1,series2)
else:
    print ("Unknown metric- " + str(key_metric))

series1="GDP growth (annual %)"
series2="Inflation, consumer prices (annual %)"
series3="Population growth (annual %)"
q=country_all_based_data(country,data2,series1,series2,series3)