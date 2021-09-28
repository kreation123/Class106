import csv 
import plotly.express as px
with open('TV_Size.csv') as f:
    df = csv.DictReader(f)
    figure  = px.scatter(df,x='TV', y ='Time')
    figure.show()