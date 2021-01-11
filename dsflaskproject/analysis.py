import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("/Users/navendrasingh/Documents/d/datasciece /covid_19_data.csv")

def get_countries():
    c = df['Country/Region'].value_counts().index
    return c



#1. show top 10 countries total recovered
#2. show top 10 countries total confirmed
#3. show top 10 countries total deaths