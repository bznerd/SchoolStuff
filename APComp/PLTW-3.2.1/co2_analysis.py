"""
Ben Campbell 11/9/22
# This program uses the pandas module to load a 2-dimensional data sheet into a pandas DataFrame object
CO2 data is displayed as a line plot
"""

import matplotlib.pyplot as plt
import pandas as pd
from math import nan

# Load in the data with read_csv()
co2_data = pd.read_csv("co2_data.csv", header=0)   # identify the header row
print(co2_data)

#Replace the unknown values with nan
co2_data['Average'] = co2_data['Average'].replace(-99.99, nan)
print(co2_data)
#Remove all enteries that have nan
co2_data.dropna(subset=['Average'], inplace=True)
print(co2_data)

#Plot the C02 data against the years
plt.plot(co2_data['Year'], co2_data['Average'], color='gray')
plt.ylabel('Average CO2 in PPM')
plt.xlabel('Years')
plt.title('Average CO2')
plt.show()
