import pandas as pd
import plotly.graph_objs as go


df = pd.read_csv('ALL UFC FIGHTERS 2_23_2016 SHERDOG.COM - Sheet1.csv')

trace = go.Scatter(
x=nom['name'],
y=localisation['locality'],
mode='markers',)


data = [trace]

