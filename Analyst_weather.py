import pandas as pd
import numpy as np
import seaborn as sns
import os
import matplotlib.pyplot as plt



df = pd.read_csv("weather_data.csv")
df["Date_Time"] = pd.to_datetime(df["Date_Time"])
location = df["Location"]

def location_analyser(region):
    data=df[df['Location']==region]
    data=data.sort_values('Date_Time')
    data=data.reset_index()
    data=data.drop('index',axis=1)
    data=data.drop('Location',axis=1)
    data=data.set_index('Date_Time')
    return data

def feature_analyzer(region,feature,rows):
    data=location_analyser(region)
    
    plt.subplot(2,1,1)
    data[feature].head(rows).plot()
    plt.axhline(data[feature].mean(),color='k',linestyle='--',linewidth=2.5)
    plt.axhline(data[feature].median(),color='g',linestyle='--',linewidth=2.5)
    plt.axhline(data[feature].mode()[0],color='m',linestyle='--',linewidth=3)
    plt.legend()
    plt.grid()
    
    plt.subplot(2,1,2)
    sns.kdeplot(data[feature].head(rows))
    plt.axvline(data[feature].mean(),color='k',linestyle='--',linewidth=2.5)
    plt.axvline(data[feature].median(),color='g',linestyle='--',linewidth=2.5)
    plt.axvline(data[feature].mode()[0],color='m',linestyle='--',linewidth=3)
    plt.legend()
    plt.grid()
    
    plt.tight_layout()
    plt.show()
    
    
print(feature_analyzer("New York" , "Temperature_C", 200))