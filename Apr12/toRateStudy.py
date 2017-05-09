#
# simple script to prepare input file for cms-l1-dpg/L1Menu
#
# @author Takashi Matsushita
#

# input file
input_file = 'L1MenuId.csv'



##  do not edit below ##
import csvtool


def menu_file(config):
  header = '''#============================================================================#          
#-------------------------------     Menu     -------------------------------#          
#============================================================================#          
# L1Seed                                                     Bit  Prescale POG    PAG 
'''

  output = file('menu.txt', 'w')
  output.write(header)
  for idx, name in config.algorithms.iteritems():
    mask = config.masks[idx] if idx in config.masks else 0
    output.write('{:60} {:>3}         {} {:6} {:6}\n'.format(name, idx, mask, config.POG[idx], config.PAG[idx]))
  output.close()

  return


if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser()
  parser.add_argument("--csv", dest="csv", default=input_file, type=str, action="store", required=False, help="path to the configuration csv file")
  parser.add_argument("--lumi", dest="mask", default="2.0", type=str, action="store", required=False, help="prescale/mask column identifier")

  options = parser.parse_args()
  config = csvtool.parse(options.csv, options.mask)

  menu_file(config)

# end
