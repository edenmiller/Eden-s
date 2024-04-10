import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

data = pd.read_csv(r'C:\Users\edenn\Documents\ISTA_131\Final_Project\annual_working_hours.csv')
us_data = data[data['Country'] == 'United States']
subset_data = data[(data['Year'] >= 1970) & (data['Year'] <= 2017)]
plt.scatter(data['Year'], data['Average annual working hours per worker'], label = 'Data', s=20, alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(data['Year'], data['Average annual working hours per worker'])
plt.plot(data['Year'], intercept + slope * data['Year'], color = 'red', label= 'Regression Line')
plt.xlabel('Year')
plt.ylabel('Average Working Hours')
plt.title('Average Annual Working Hours in the US (1870 - 2017)')
plt.gca().get_xaxis().get_major_formatter().set_useOffset(False)
plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
plt.legend()
plt.show()