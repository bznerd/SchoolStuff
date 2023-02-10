"""
Ben Campbell 11/14/22
PLTW 3.2.2
"""
# This program uses the pandas module to load a 3-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot comparative line graphs 

import matplotlib.pyplot as plt
import pandas as pd

# choose countries of interest
my_countries = ['United States', 'Zimbabwe','Cuba', 'Caribbean small states', "Cameroon", "Burundi"]

# Load in the data with read_csv()
df = pd.read_csv("elec_access_data.csv", header=0)    # header=0 means there is a header in row 0

# get a list unique countries
unique_countries = df['Entity'].unique()

# Plot the data on a line graph passed a title and marker types in a list
def make_plot(title, markers):
  for c in unique_countries:
    if c in my_countries:
      # match country to one of our we want to look at and get a list of years
      years = df[df['Entity'] == c]['Year']

      # match country to one of our we want to look at and get a list of electriciy values
      sum_elec = df[df['Entity'] == c]['Access']

      #Make the plot
      plt.plot(years, sum_elec, label=c, marker=markers[my_countries.index(c)], linestyle='--')

  plt.ylabel('Percentage of Country Population')
  plt.xlabel('Year')
  plt.title(title + '\nPercent of Population with Access to Electricity')
  plt.legend()
  plt.show()

#For each request graph set the countries list and then plot the data
make_plot('Generic',['o', 'v', 'X', 'X', 'v', 'v'])
my_countries = ['United States', 'Canada', 'Mexico', 'Cuba', 'Brazil', 'Argentina']
make_plot('North vs. South America', ['o','o','o','X','X','X'])
my_countries = ['United Kingdom', 'France', 'Germany', 'Italy', 'Spain', 'Portugal']
make_plot('Europe', ['P','P','P','P','P','P'])
my_countries = ['China', 'Japan', 'Thailand', 'Vietnam', 'South Korea', 'Singapore']
make_plot('Asia', ['<','<','<','<','<','<'])
my_countries = ['Cameroon', 'Burundi', 'Zimbabwe', 'South Africa', 'Ethiopia', 'Rwanda']
make_plot('Africa', ['v','v','v','v','v','v'])
