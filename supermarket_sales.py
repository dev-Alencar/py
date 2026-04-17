import pandas as pd
import plotly.express as px



# Link direto do GitHub 
df = pd.read_csv('https://raw.githubusercontent.com/sushantag9/Supermarket-Sales-Data-Analysis/master/supermarket_sales%20-%20Sheet1.csv')


fig = px.histogram(df, x='Product line', y='Total', color='Gender')

fig.show() 