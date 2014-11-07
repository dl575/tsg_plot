#!/usr/bin/python

import sys
sys.path.extend(['../..'])
import tsg_plot
import math

opts = tsg_plot.PlotOptions()

attribute_dict = \
    {
        'data' : [
          [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
          [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25]],
          [[1, 1], [2, 2], [3, 3], [4, 2], [5, 1]],
          ],
        'plot_type' : 'scatter'
    }

for name, value in attribute_dict.iteritems():
  setattr( opts, name, value )
tsg_plot.add_plot( opts )
