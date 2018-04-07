import pandas as pd

"""
Modify the cities table by adding a new boolean column that is True 
if and only if both of the following are True:

- The city is named after a saint.
- The city has an area greater than 50 square miles.
"""

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

cities = pd.DataFrame({ 'City name': city_names, 'Population': population })

print ("\n🏢  Great Saint cities")
cities['Is Great and Saint'] = (cities['Population'] > 50) & cities['City name'].apply(
    lambda val: val.startswith('San')
)

print (cities)