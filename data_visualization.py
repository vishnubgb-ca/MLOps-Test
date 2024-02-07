from data_preprocessing import date_preprocessing
import matplotlib.pyplot as plt
# import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.io as pio
import io
from PIL import Image


def data_visualizations():    
    print("............In  data_visualization............")
    data = date_preprocessing()
    #boxplot
    fig = px.box(data, y=["Temperature", "Current"])
    fig.update_layout(template='plotly_dark')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False,zeroline=True,zerolinewidth=4)
    try:
        pio.write_image(fig, 'boxplot.jpg', engine='kaleido')
    except (ValueError, ImportError):
        pio.write_image(fig, 'boxplot.jpg') 
    # fig.write_image("boxplot.jpg")

    #linechart
    fig = px.line(data, x="datetime", y=["Temperature","Current"])
    fig.update_layout(template='plotly_dark')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False,zeroline=True,zerolinewidth=4)
    try:
        pio.write_image(fig, 'linechart.jpg', engine='kaleido')
    except (ValueError, ImportError):
        pio.write_image(fig, 'linechart.jpg') 
    # fig.write_image("line_chart.jpg")
    
    return data

data_visualizations()