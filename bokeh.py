from numpy.random import random
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import column, widgetbox
from bokeh.models import Button, ColumnDataSource

fig = figure(title='random data', width=500, height=200,
             tools='pan,box_zoom,reset,save')

source = ColumnDataSource(data={'x': [], 'y': []})
fig.line('x', 'y', source=source)

def click(n=100):
    source.data = {'x': range(n), 'y': random(n)}

button = Button(label='update', button_type='success')
button.on_click(click)
