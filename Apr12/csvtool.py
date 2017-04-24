#!/bin/env python

import csv
import sys

MAX_INDEX = 512


class Config:
  def __init__(self):
    pass


def parse(input_file):
  import inspect
  fname = "%s.%s(%s)" % (__name__, inspect.currentframe().f_code.co_name, input_file)

  config = Config()

  indicies = set()
  seeds = set()
  config.masks = {}
  config.algorithms = {}


  # parse input file with the format <id>, <name>, ..., <mask>, ...
  with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      idx = None
      try:
        idx = int(row['id'])
      except:
        print 'ERROR in %s: index undefined: %s' % (fname, row)
        sys.exit(1)

      if idx < 0 or idx >= MAX_INDEX:
        print 'ERROR in %s: index out of range: %s' % (fname, row)
        sys.exit(1)

      if idx in indicies:
        print 'ERROR in %s: index duplicated: %s' %(fname, row)
        sys.exit(1)

      name = row['name']
      if not name.startswith('L1_'):
        print "ERROR in %s: name not start with L1_ '%s'" % (fname, name)
        sys.exit(1)

      length = len(name)
      if length != len(name.strip()):
        print "ERROR in %s: name end with whites '%s'" % (fname, name)
        sys.exit(1)

      if name in seeds:
        print "ERROR in %s: name duplicated '%s'" % (fname, name)
        sys.exit(1)

      indicies.add(idx)
      seeds.add(name)

      if int(row['mask']) == 1: config.masks[idx] = 1
      config.algorithms[idx] = name

  return config

# eof
