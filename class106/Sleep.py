import csv
import plotly.express as px
with open('Sleep.csv') as f :
    df = csv.DictReader(f)
    figure = px.scatter(df , x='Coffee in ml', y = 'sleep in hours')
    figure.show()