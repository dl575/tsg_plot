#!/usr/bin/python

import sys
sys.path.extend(['../..'])
import tsg_plot
import math

# Parse data
f = open("example_histogram.csv", 'r')
data = []
for line in f:
  data.append([float(x) for x in line.strip().split(',')])
f.close()

# Set up plotting options
opts = tsg_plot.PlotOptions()
opts.data = data

attribute_dict = \
    {
        'plot_type' : 'histogram',
        'histogram_bins' : 25,

        'show' : False,
        'file_name' : 'example_histogram.pdf',
        'figsize' : (3.5, 2.5),

        'xlabel' : 'Value',
        'ylabel' : 'Count',
        'fontsize' : 8,

        'legend_enabled' : True,
        'legend_ncol' : 3,
        'labels' : ["Uniform", "Gaussian", "Weibull"],
    }
for name, value in attribute_dict.iteritems():
  setattr( opts, name, value )

# Plot
tsg_plot.add_plot( opts )

