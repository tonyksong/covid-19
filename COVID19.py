import pandas as pd
from plotly import graph_objs as go
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('mode.chained_assignment', None)

# Read in data for death cases
deaths=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv')

# Filter for deaths in US
US_deaths = deaths.loc[deaths['Country/Region'] == 'US']

# Read in data for confirmed cases
confirmed=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')

# Filter for confirmed cases in US
US_confirmed = confirmed.loc[confirmed['Country/Region'] == 'US']

# Filter for confirmed cases in NY
NY_confirmed = US_confirmed.loc[US_confirmed['Province/State'] == 'New York']

# Pivot NY_confirmed
NY_confirmed_pivot = NY_confirmed.T

NY_confirmed_pivot.loc['3/10/20']

# Filter data to only include dates after 3/10/20
NY_conf_cases = NY_confirmed_pivot.iloc[51:]

#NYC_confirmed = US_confirmed.loc[US_confirmed['Province/State'] == 'New York County, NY']

NY_deaths = US_deaths.loc[US_deaths['Province/State'] == 'New York']

# Filter data to only include dates after 3/10/20
NY_deaths = NY_deaths.T.iloc[51:]

# Read in data for recovered cases
recovered=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv')

NY_recovered = recovered.loc[recovered['Province/State'] == 'New York']

# Create NY dataframe with columsn for confirmed cases and deaths
NY = NY_conf_cases + NY_deaths
NY['Confirmed Cases'] = NY_conf_cases
NY['Deaths'] = NY_deaths

# Drop unnecessary column
NY.drop(99, axis=1, inplace=True)

# Convert the index to datetime format
NY.index = pd.to_datetime(NY.index)

# Plot deaths and confirmed cases
fig, ax = plt.subplots(figsize=(15,7))
ax.set(xlabel="Date", ylabel="Number of Cases")
plot=NY.plot(title='COVID-19 in New York', ax=ax, grid=True)

# Add labels to data points for Confirmed Cases
for i,j in NY['Confirmed Cases'].items():
    ax.annotate(str(int(j)), xy=(i, j))

# Add labels to data points for Deaths
for i,j in NY['Deaths'].items():
    ax.annotate(str(int(j)), xy=(i, j))

# Save plot as test.svg
plt.savefig("test.svg")


