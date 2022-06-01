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
data['Released'] = data['Released'].apply(pd.to_datetime) #transforms our string values in column Released into a datetime object
data = data.sort_values(by='Released') #sorts our released column 

def format_title(title):
  # if('…' in title):
  #   print('incomplete title')
  #   print(title)

  #handle special cases
  if("F9" in title):
    return ["F9", "fast 9", "fast and furious 9", "f9 the fast saga"]
  if("Shang-Chi" in title):
    return ["shang chi", "shang chi and the legend of the ten rings"]
  if("Summer of Soul" in title):
    return ["summer of soul", "summer of soul or when the revolution cannot be televised"]
  if("Roadrunner" in title):
    return ['Roadrunner', 'roadrunner anthony bourdain', 'road runner a film about anthony bourdain']
  if("Christmas with the Chosen" in title):
    return ["Christmas with the chosen", 'christmas with the chosen the messengers']
  if("Quiet Place" in title):
    return ["a quiet place", "a quiet place part 2", "a quiet place part II"]

  to_return = []
  
  #handle dashes
  title = title.replace("-", " ")
  # handle colons
  colon_split = title.split(':')
  if(len(colon_split) > 1):
    to_return.append(colon_split[0])
    to_return.append(" ".join(colon_split).replace("  ", " "))
  else:
    to_return.append(title)
  

  return to_return

for index,row in data.iterrows():
    title = row['Title']
    words = title.split()
    if(len(words) == 1):
        continue

    since = (row['Released'] - datetime.timedelta(days=365)).strftime('%Y-%m-%d')
    until = row['Released'].strftime('%Y-%m-%d')
    filename = str(index) + '-' + title.lower().replace(' ', '')
    filename += '.txt'


    titles = format_title(title)
    for formatted_title in titles:
      command = 'snscrape --jsonl --since ' + since + ' twitter-search "' + formatted_title + ' movie until:' + until + '" > raw_tweets/' + filename
      os.system(command)

# we format titles for scraping
# check for with and without colons
# special handling for certain cases
