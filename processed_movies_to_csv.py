import os
import pandas as pd
import datetime

data = pd.read_csv('MovieReport.csv')
data.head()

data = data.rename(columns={"Domestic\r\nBox Office":"Domestic Box Office", "International\r\nBox Office":"International Box Office", 
            "Worldwide\r\nBox Office":"Worldwide Box Office"}) #simple renaming of columns so it can be easier to read

# Jan 27, 2021
# 01/27/2021
def standarize_date(str): #This function is what we apply to our dataframe column Released in order to change the formatting of the date
  try:
    str = str.strip()

    str = str.replace('Jan ', "01/")
    str = str.replace('Feb ', "02/")
    str = str.replace('Mar ', "03/")
    str = str.replace('Apr ', "04/")
    str = str.replace('May ', "05/")
    str = str.replace('Jun ', "06/")
    str = str.replace('Jul ', "07/")
    str = str.replace('Aug ', "08/")
    str = str.replace('Sep ', "09/")
    str = str.replace('Oct ', "10/")
    str = str.replace('Nov ', "11/")
    str = str.replace('Dec ', "12/")

    str = str.replace(', ', "/")

    str = str.replace('/1/', "/01/")
    str = str.replace('/2/', "/02/")
    str = str.replace('/3/', "/03/")
    str = str.replace('/4/', "/04/")
    str = str.replace('/5/', "/05/")
    str = str.replace('/6/', "/06/")
    str = str.replace('/7/', "/07/")
    str = str.replace('/8/', "/08/")
    str = str.replace('/9/', "/09/")

    out = str
  except:
    out = "n/a" 

  return out

data['Released'] = data['Released'].apply(standarize_date) # applies our transformation for the dates so that we can then sort them by ascending

data.to_csv('processed_movies.zip',index=False)
data['Released'] = data['Released'].apply(pd.to_datetime) #transforms our string values in column Released into a datetime object
