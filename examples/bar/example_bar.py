#!/usr/bin/python

import sys
sys.path.extend(['../..'])
import tsg_plot
import math

opts = tsg_plot.PlotOptions()

attribute_dict = \
    {
        'data' : [[1, 2, 3, 4, 5],
                  [1, 4, 9, 16, 25],
                  [1, 2, 3, 2, 1]
                  ],
    }

for name, value in attribute_dict.iteritems():
  setattr( opts, name, value )
tsg_plot.add_plot( opts )
