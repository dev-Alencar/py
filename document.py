import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv')

fig = px.line(df,
              x='Year',
              y='Value',
              title='Dados de GDP para estudo',
              markers=True)

fig.show()