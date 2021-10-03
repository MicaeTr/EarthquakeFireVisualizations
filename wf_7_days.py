import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data
filename = 'world_fires_7_day.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        brights, lons, lats, hover_texts = [], [], [], []
    for row in reader:
        try:
            lat = float(row[0])
            lon = float(row[1])
            bright = float(row[2])
        except ValueError:
            print(f"Missing data for {row}")
        else:
            brights.append(bright)
            lons.append(lon)
            lats.append(lat)

# Map the fires

data = [Scattergeo(lon=lons, lat=lats)]
graph_name = 'World Fires'

my_layout = Layout(title=graph_name)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')
