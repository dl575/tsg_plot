#!/usr/bin/python

import sys
sys.path.extend(['../..'])
import tsg_plot
import math

def parse(filename):
  f = open(filename, 'r')

  data = []
  for line in f:
    data.append(map(float, line.split(',')))

  f.close()

  return data

def plot(data):
  opts = tsg_plot.PlotOptions()
  opts.data = data

  attribute_dict = \
      {
          'labels' : ['line 1', 'line 2', 'line 3'],
          'show' : False,
          'file_name' : 'example_line.pdf',
          'plot_type' : 'line',
          'figsize' : (7.0, 3.0),
          'legend_ncol' : 3,
          'xlabel' : 'x',
          'ylabel' : 'f(x)',
          'symbols' : ['.']*3,
          'linestyles' : ['-', '', '--'],
          'markersize' : 8,
      }

  for name, value in attribute_dict.iteritems():
    setattr( opts, name, value )
  tsg_plot.add_plot( opts )

if __name__ == "__main__":
  data = parse("example_line.csv")
  plot(data)
