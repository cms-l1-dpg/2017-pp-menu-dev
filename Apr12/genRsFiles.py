#
# simple script to prepare run-setting files from L1MenuId.csv file
#
# @author Takashi Matsushita
#

# prescale columns
ps_columns = ('2.0', '1.45')

# input file
input_file = 'L1MenuId.csv'



##  do not edit below ##
import csvtool

def mask_file(config):
  rows = ""
  for ii in range(csvtool.MAX_INDEX):
    if ii in config.algorithms:
      rows += "        <row>%d,%d</row> <!-- %s -->\n" % (ii, 1, config.algorithms[ii])
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


def prescale_file(config):
  header = "      <columns>algo/prescale-index"
  types = "      <types>uint"
  comment = "<!-- id[lumi in e34]"
  n_columns = len(config.prescales)
  for ii in range(n_columns):
    header += ", %d" % ii
    types += ", uint"
    comment += ", %s[%s]" % (ii, config.ps_columns[ii])
  header += "</columns>"
  types += "</types>"
  comment += " -->"

  rows = ""
  for ii in range(csvtool.MAX_INDEX):
    if ii in config.algorithms:
      rows += "        <row>%d" % ii
      for key in config.prescales:
        ps = int(config.prescales[key][ii])
        rows += ",%d" % ps
      rows += "</row> <!-- %s -->\n" % config.algorithms[ii]
  rows = rows.strip('\n')

  prescale = {}
  prescale['header'] = header
  prescale['rows'] = rows
  prescale['types'] = types
  prescale['comment'] = comment

  template = """<?xml version="1.0" encoding="UTF-8"?>
<run-settings id="uGT">
  <context id="uGtProcessor">
    <param id="index" type="uint">0</param>
    <param id="prescales" type="table">
%(header)s %(comment)s
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
  import argparse

  parser = argparse.ArgumentParser()
  parser.add_argument("--csv", dest="csv", default=input_file, type=str, action="store", required=False, help="path to the configuration csv file [default: %s]" % input_file)
  parser.add_argument("--lumi", dest="mask", default=ps_columns, type=str, nargs='+', action="store", required=False, help="prescale/mask column identifier [default: %s]" % ' '.join(ps_columns))

  options = parser.parse_args()
  config = csvtool.parse(options.csv, options.mask)

  mask_file(config)
  prescale_file(config)

# end
