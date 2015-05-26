#!/usr/bin/python

import sys
sys.path.extend(['../..'])
import tsg_plot
import math

# Parse data
f = open("example_boxplot.csv", 'r')
data = []
for line in f:
  data.append([float(x) for x in line.strip().split(',')])
f.close()

# Set up plotting options
opts = tsg_plot.PlotOptions()
opts.data = data

attribute_dict = \
    {
        'plot_type' : 'boxplot',

        'show' : False,
        'file_name' : 'example_boxplot.pdf',
        'figsize' : (3.5, 2.5),

        # Color are optional, default is black
        'boxplot_color_boxes'    : '#e41a1c',
        'boxplot_color_medians'  : '#377eb8',
        'boxplot_color_whiskers' : '#4daf4a',
        'boxplot_color_caps'     : '#984ea3',
        'boxplot_color_fliers'   : '#ff7f00',
        'boxplot_fliers_size' : 10,

        'xlabel' : 'Distribution',
        'ylabel' : 'Value',
        'fontsize' : 8,
        'labels' : ["Uniform", "Gaussian", "Weibull"],
    }
for name, value in attribute_dict.iteritems():
  setattr( opts, name, value )

# Plot
tsg_plot.add_plot( opts )

