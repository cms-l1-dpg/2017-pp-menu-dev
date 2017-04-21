#
# simple script to prepare run-setting files from L1MenuId.csv file
#
# @author Takashi Matsushita
#

# number of prescale columns
n_columns = 2

# input file
input_file = 'L1MenuId.csv'



##  do not edit below ##
MAX_INDEX = 512

def mask_file(masks):
  rows = ""
  for ii in range(MAX_INDEX):
    if ii in masks:
      rows += "        <row>%d,%d</row>\n" % (ii, masks[ii])
    else:
      rows += "        <row>%d,%d</row>\n" % (ii, 0)
  rows = rows.strip('\n')

  template = """<run-settings id="uGT">
  <context id="uGtProcessor">
    <param id="finorMask" type="table">
      <columns>
 	      algo,mask
      </columns>
      <types>
 	      uint,uint
      </types>
      <rows>
%s
      </rows>
    </param>
  </context>
</run-settings>
"""

  output = file('mask.xml', 'w')
  output.write(template % rows)
  output.close()

  return


def prescale_file(algorithms):
  header = "      <columns>algo/prescale-index"
  types = "      <types>uint"
  for ii in range(n_columns):
    header += ", %d" % ii
    types += ", uint"
  header += "</columns>"
  types += "</types>"

  rows = ""
  for ii in range(MAX_INDEX):
    if ii in algorithms:
      rows += "        <row>%d" % ii
      for jj in range(n_columns):
        rows += ",1"
      rows += "</row>\n"
  rows = rows.strip('\n')

  prescale = {}
  prescale['header'] = header
  prescale['rows'] = rows
  prescale['types'] = types

  template = """<?xml version="1.0" encoding="UTF-8"?>
<run-settings id="uGT">
  <context id="uGtProcessor">
    <param id="index" type="uint">0</param>
    <param id="prescales" type="table">
%(header)s
%(types)s
      <rows>
%(rows)s
      </rows>
    </param>
  </context>
</run-settings>
"""

  output = file('prescale.xml', 'w')
  output.write(template % prescale)
  output.close()

  return


if __name__ == '__main__':
  import csv
  import sys

  indicies = set()
  masks = {}
  algorithms = {}

  # parse input file with the format <id>, <name>, ..., <mask>, ...
  with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      idx = None
      try:
        idx = int(row['id'])
      except:
        print "inf> skipping: ", row
        continue

      if idx < 0 or idx >= MAX_INDEX:
        print 'err> index undefined ', row
        sys.exit(1)

      if idx in indicies:
        print 'err> index duplicated ', row
        sys.exit(1)

      if int(row['mask']) == 1: masks[idx] = 1
      algorithms[idx] = row['name']

  mask_file(masks)
  prescale_file(algorithms)

# end
