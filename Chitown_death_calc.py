
# coding: utf-8

# In[89]:


import csv
f = open("guns.csv", 'r')
csvreader = csv.reader(f)
data = list(csvreader)
#print(data[:4])
#complete - Excersize 1


# In[90]:


headers = data[0]
data = data[1:]
#print(headers)
#print(data[:5])
#complete - Excersize 2


# In[91]:


years = [row[1] for row in data]
year_counts = {}
for year in years: 
    if year not in year_counts: 
        year_counts[year]=1
    else:
        year_counts[year]+=1
#print(year_counts)
#complete excersize 3
#deaths count by year



# In[92]:


import datetime
dates = [datetime.datetime(year=int(row[1]),month=int(row[2]), day=1) for row in data]
#print(dates[:5])
#excersize 4
date_counts = {}
for date in dates: 
    if date not in date_counts:
        date_counts[date] = 1
    else: 
        date_counts[date] +=1
#print(date_counts)
#excersize 4


# In[93]:


def gun_death_counts(row_num):
    var=[row[row_num] for row in data]
    dict_var = {}
    for v in var:
        if v not in dict_var:
            dict_var[v] = 1
        else:
            dict_var[v] +=1
    return dict_var
intent_counts = gun_death_counts(3)
police_counts = gun_death_counts(4)
sex_counts = gun_death_counts(5)
age_counts = gun_death_counts(6)
race_counts = gun_death_counts(7)
hispanic_counts = gun_death_counts(8)
place_counts = gun_death_counts(9)
education_counts = gun_death_counts(10)

#number 5


# In[94]:


f2 = open("census.csv", 'r')
csvreader2 = csv.reader(f2)
census_data = list(csvreader2)
#print(census_data)
#excersize 6


# In[95]:


print(race_counts)


# In[96]:


c_f = open("census.csv", 'r')
csvreader_c_f = csv.reader(c_f)
census = list(csvreader_c_f)
#print(census)


# In[103]:


mapping = {
    'Asian/Pacific Islander': 15159516+674625,
    'White':197318956,
    'Native American/Native Alaskan':3739506,
    'Black': 40250635,
    'Hispanic':44618105,
}

race_per_hundredk = {}
for key, value in race_counts.items(): 
    race_per_hundredk[key] = (value/mapping[key])*100000
#print(race_per_hundredk)
print(intent_counts)
    
    


# In[113]:


intents = [row[3] for row in data]
races = [row[7] for row in data]

homicide_race_counts = {}
for i, race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == 'Homicide':
        homicide_race_counts[race] +=1
#print(homicide_race_counts)
race_per_hundredk_homicide = {}

for key, value in homicide_race_counts.items():
    race_per_hundredk_homicide[key] = (value/mapping[key])*100000
print(race_per_hundredk_homicide)



