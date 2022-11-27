import pandas as pd

#To remove unecessary cities
df = pd.read_csv('city_temperature.csv')
index = df[(df['City']=='Charleston') | (df['City']== 'Amarillo') | (df['City']== 'Brownsville') | (df['City']=='San Antonio') | (df['City']=='Norfolk') | (df['City']== 'Syracuse')].index
df.drop(index , inplace=True)
df.to_csv('DailyTemperatures.csv',index=False)

#To remove NULL Values (AvgTemperature=-99)
df = pd.read_csv('DailyTemperatures.csv')
index = df[df['AvgTemperature']==-99].index
df.drop(index , inplace=True)
df.to_csv('DailyTemperatures.csv',index=False)

#To display all Regions, Countries, Cities and CityCodes in CSV File
df=pd.read_csv('DailyTemperatures.csv')
print(df['Country'].unique())
print(df['City'].unique())
print(df['CityCode'].unique())
print(df['Region'].unique())

#To give City Names a corresponding CityCode
df = pd.read_csv('DailyTemperatures.csv')
y = df['City'].factorize()[0]
df.insert(2,column='CityCode',value=y)
df.to_csv('DailyTemperatures.csv',index=False)

#To replace City Names
df=pd.read_csv('DailyTemperatures.csv')
df.City.replace('San Juan Puerto Rico', 'San Juan (Puerto Rico)', inplace=True)
df.to_csv('DailyTemperatures.csv',index=False)
