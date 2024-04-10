import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

data = pd.read_csv(r'C:\Users\edenn\Documents\ISTA_131\Final_Project\COVID-19_Vaccinations_in_the_US.csv')
filtered_data = data[['Location', 'Distributed']]
plt.figure(figsize=(12,6))
plt.bar(filtered_data['Location'], filtered_data['Distributed'])
plt.xticks(rotation=90)
def millions_formatter(x, pos):
    return '{:.0f}M'.format(x / 1e6)
plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
plt.xlabel('States/Territories')
plt.ylabel('Total Distributed Doses (Millions)')
plt.title('Total Distributed COVID-19 Vaccine Doses in US States/Territories')
plt.tight_layout()
plt.show()