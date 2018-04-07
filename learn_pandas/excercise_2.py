import pandas as pd

"""
The reindex method allows index values that are not in the original DataFrame's index values. 
Try it and see what happens if you use such values! 
Why do you think this is allowed?
"""

index = ['San Francisco', 'San Jose', 'Sacramento']

cities = pd.DataFrame({'Population': [852469, 1015785, 485199] }, index=index)

cities['Area square miles'] = [46.87, 176.53, 97.92]
cities['Population density'] = cities['Population'] / cities['Area square miles']

print (
    cities.reindex(
        index=['San Francisco', 'San Jose', 'Sacramento', 'Pistoia'], 
        fill_value=0
    )
)