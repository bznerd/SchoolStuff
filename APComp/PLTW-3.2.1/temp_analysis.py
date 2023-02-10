"""
Ben Campbell 11/9/22
# This program uses the pandas module to load a 2-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot a graph and a bar chart
"""

import matplotlib.pyplot as plt
import pandas as pd

# Load in the data with read_csv()
temp_data = pd.read_csv("temperature_data.csv", header=0)   # identify the header row

#Plot the raw temperature data
plt.plot(temp_data['Year'], temp_data['Anomaly'], color='gray')
plt.ylabel('Temperature Anomalies in Celsius')
plt.xlabel('Years')
plt.title('Change in Temperatures')

#Plot the smoothed temperature data
plt.plot(temp_data['Year'], temp_data['LOWESS'], color='red')
plt.show()

#Plot the raw temperature data as a bar chart instead of line plot
plt.bar(temp_data['Year'], temp_data['Anomaly'], align='center', color='green')
plt.ylabel('Temperature Anomalies in Celsius')
plt.xlabel('Years')
plt.title('Change in Temperatures')
plt.show()

#Initialize min, max, sum, and averages
min_anomaly = temp_data['Anomaly'][0]
max_anomaly = temp_data['Anomaly'][0]
min_year = temp_data['Year'][0]
max_year = temp_data['Year'][0]
sum_anomaly = 0
avg_anomaly = 0

#Calculate min max and sum by looping over all data
for i in range(len(temp_data['Anomaly'])):
  if (temp_data['Anomaly'][i] < min_anomaly):
    min_anomaly = temp_data['Anomaly'][i]
    min_year = temp_data['Year'][i]

  if (temp_data["Anomaly"][i] > max_anomaly):
    max_anomaly = temp_data["Anomaly"][i]
    max_year = temp_data["Year"][i]
  
  sum_anomaly += temp_data["Anomaly"][i]

#Calculate the average anomaly and print all values to terminal
avg_anomaly = sum_anomaly/len(temp_data["Anomaly"])
print(f"Min Anomaly: {min_anomaly}, Year: {min_year}")
print(f"Max Anomaly: {max_anomaly}, Year: {max_year}")
print(f"Average anomaly: {avg_anomaly}")
