#*************************************
#
#   File:           skill006.py
#   Author:         Cynthia Drake
#   Skill:          6
#   Create Date:    10/01/2019
#   Last Modified:  10/01/2019
#
#*************************************

import pandas as pd
from matplotlib import pyplot as plt

url = "https://raw.githubusercontent.com/datasets/gdp/0be54c18d900edc37123f25b4eff014731c9e459/data/gdp.csv"  
data = pd.read_csv(url)

data.columns = [c.replace(' ','_') for c in data.columns]

us = data[data.Country_Name == 'United States']
eu = data[data.Country_Name == 'European Union']
china = data[data.Country_Name == 'China']

plt.plot(us.Year, us.Value / 10**9, 'b', linewidth=4)
plt.plot(eu.Year, eu.Value / 10**9, '--g', linewidth=3)
plt.plot(china.Year, china.Value / 10**9, 'or')

plt.legend(['United States', 'EU', 'China'])
plt.xlabel('Year')
plt.ylabel('GDP')
plt.title("Cynthia Drake's GDP Plot")
plt.show()
