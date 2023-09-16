import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  # Create scatter plot
  plt.scatter(df.Year, df['CSIRO Adjusted Sea Level'])
  plt.xlabel('Year')
  plt.ylabel('CSIRO Adjusted Sea Level')

  # Linear regression
  # Using stats.linregress to fit data
  FirstRes = linregress(df.Year, df['CSIRO Adjusted Sea Level'])

  # Create first line of best fit
  # The data frame only strict from year 1880 to 2013. In order to plot to year 2051, the new line must be created.
  x_var = np.arange(df['Year'].min(), 2051, 1)
  plt.plot(x_var,
           FirstRes.slope * x_var + FirstRes.intercept,
           'r',
           label='fitted-1')
  # As the result, the fitting data could not described the data beyond year 2013

  # Create second line of best fit
  # Select data from year 2000 to correct the fitting data (as much as possible)
  df_new = df[df['Year'] >= 2000]
  NewRes = linregress(df_new.Year, df_new['CSIRO Adjusted Sea Level'])
  new_x_var = np.arange(df_new['Year'].min(), 2051, 1)
  plt.plot(new_x_var,
           NewRes.slope * new_x_var + NewRes.intercept,
           'k',
           label='fitted-2')

  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
  #plt.legend()
  # P.S. I try to use legend but it seem the repetitions occur which not the same as my notebook. Therefore, I will comment this part out of the code.
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
