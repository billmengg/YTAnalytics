import pandas as pd

#Load files
content = pd.read_csv('Project/Content.csv')
cities = pd.read_csv('Project/Cities.csv')
date = pd.read_csv('Project/Date.csv')
source = pd.read_csv('Project/Traffic source.csv')

#Remove first row (totals)
content = content.iloc[1:]
cities = cities.iloc[1:]
date = date.iloc[1:]
source = source.iloc[1:]

#Datetime
content['Video publish time'] = pd.to_datetime(content['Video publish time'])
content['Duration'] = pd.to_timedelta(content['Duration'], unit='s')
content['Watch time (hours)'] = pd.to_timedelta(content['Watch time (hours)'], unit='h')
content['Average view duration'] = pd.to_timedelta(content['Average view duration'])
content['Impressions click-through rate (%)'] = content['Impressions click-through rate (%)'] / 100
content.rename(columns={'Impressions click-through rate (%)': 'Impressions CTR'}, inplace=True)

date['Date'] = pd.to_datetime(date['Date'])
date['Watch time (hours)'] = pd.to_timedelta(date['Watch time (hours)'], unit='h')
date['Average view duration'] = pd.to_timedelta(date['Average view duration'])

cities['Watch time (hours)'] = pd.to_timedelta(cities['Watch time (hours)'], unit='h')
cities['Average view duration'] = pd.to_timedelta(cities['Average view duration'])

source['Watch time (hours)'] = pd.to_timedelta(source['Watch time (hours)'], unit='h')
source['Average view duration'] = pd.to_timedelta(source['Average view duration'])
source['Impressions click-through rate (%)'] = source['Impressions click-through rate (%)'] / 100
source.rename(columns={'Impressions click-through rate (%)': 'Impressions CTR'}, inplace=True)

print(content.head())
