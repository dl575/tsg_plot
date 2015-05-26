#!/usr/bin/python

import sys
sys.path.extend(['../..'])
import tsg_plot
import math

# Parse data
f = open("example_bar.csv", 'r')
subcat = f.readline().strip().split(',')[1:]
cat = []
data = []
for line in f:
  ls = line.split(',')
  cat.append(ls[0])
  data.append([float(x) for x in ls[1:]])
f.close()

# Set up plotting options
opts = tsg_plot.PlotOptions()
opts.data = data
opts.labels = [cat, subcat]

attribute_dict = \
    {
        'show' : False,
        'file_name' : 'example_bar2.pdf',
        'figsize' : (3.5, 2.5),
        'fontsize' : 8,
        'xlabel' : 'Functions',
        'ylabel' : 'Value',
        'legend_ncol' : 3,
        'rotate_labels' : True,
        'rotate_labels_angle' : -30,
        'yrange' : [0, 20],
        'overflow_labels_enabled' : True,
        'legend_bbox' : [0, 1.1, 1, 0.1],
    }
for name, value in attribute_dict.iteritems():
  setattr( opts, name, value )

# Plot
tsg_plot.add_plot( opts )
