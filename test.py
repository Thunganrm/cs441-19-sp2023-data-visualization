import plotly.graph_objects as go
import pandas as pd
from worldometer import api
import matplotlib.animation as animation

def get_death_data():
    data = {
        'Deaths caused by HIV/AIDS this year': api.deaths_caused_by_hiv_aids_this_year()['deaths_caused_by_hiv/aids_this_year'],
        'Deaths caused by cancer this year': api.deaths_caused_by_cancer_this_year()['deaths_caused_by_cancer_this_year'],
        'Deaths caused by malaria this year': api.deaths_caused_by_malaria_this_year()['deaths_caused_by_malaria_this_year'],
        'Deaths caused by smoking this year': api.deaths_caused_by_smoking_this_year()['deaths_caused_by_smoking_this_year']
    }
    return data

# Get the death data from the API
data = get_death_data()
causes = list(data.keys())
deaths = list(data.values())

# Create a bar chart object
fig = go.Figure(data=[go.Bar(x=causes, y=deaths)])

# Set the title and axis labels
fig.update_layout(title="Number of Deaths by Cause",
                  xaxis_title="Causes",
                  yaxis_title="Number of Deaths")

# Display the chart
fig.show()



