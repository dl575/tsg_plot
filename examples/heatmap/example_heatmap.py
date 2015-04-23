#!/usr/bin/python

import sys
sys.path.extend(['../..'])
import tsg_plot
import math

# Generate data
n = 11
data = [[0]*n for i in range(n)]
for i in range(n):
  for j in range(n):
    data[i][j] = i+j

# Set up plotting options
opts = tsg_plot.PlotOptions()
opts.data = data

attribute_dict = \
    {
        'plot_type' : 'heatmap',

        'show' : False,
        'file_name' : 'example_heatmap.pdf',
        'figsize' : (3.5, 3.5),

        'xlabel' : 'x value',
        'ylabel' : 'y value',
        'fontsize' : 8,

        'heatmap_cbar' : True,
        'heatmap_cbar_label' : 'x + y',
        'heatmap_cbar_shrink' : 0.65,

        'yrange' : [-0.5, 10.5],
        'xrange' : [-0.5, 10.5],
    }
# The heatmap_cmap is interpreted in the following way:
#   For each color component (red, green, blue) we have a list. Each item in
#   the list specifies a point in the color map: (data value, start color
#   value, end color value). All values are specified in [0, 1]. The <start
#   color value> indicates that for data points less than <data value>, their
#   color will be linearly scaled up to <start color value> at <data value>.
#   For data points greater than <data value>, their color will start at <end
#   color value> and be scaled up from there to the next specified point.
opts.heatmap_cmap = {
    'red' : [(0, 239./255, 239./255), (1, 8./255, 8./255)],
    'green' : [(0, 243./255, 243./255), (1, 81./255, 81./255)],
    'blue' : [(0, 255./255, 255./255), (1, 156./255, 156./255)]
    }

for name, value in attribute_dict.iteritems():
  setattr( opts, name, value )

# Plot
tsg_plot.add_plot( opts )

