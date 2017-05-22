#
# simple script to prepare input file for cms-l1-dpg/L1Menu
#
# @author Takashi Matsushita
#

# defaults
input_file = 'L1MenuId.csv'
ps_column = '2.0'


##  do not edit below ##
import csvtool


def menu_file(config, options):
  header = '''#============================================================================#          
#-------------------------------     Menu     -------------------------------#          
#============================================================================#          
# L1Seed                                                     Bit  Prescale POG    PAG 
'''

  output = file('menu.txt', 'w')
  output.write(header)
  for idx, name in config.algorithms.iteritems():
    ps = 0 if (options.unprescaled and config.prescales[options.mask][idx] != 1) else config.prescales[options.mask][idx]
    output.write('{:60} {:>3}         {} {:6} {:6}\n'.format(name, idx, ps, config.POG[idx], config.PAG[idx]))
  output.close()

  return


if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser()
  parser.add_argument("--csv", dest="csv", default=input_file, type=str, action="store", required=False, help="path to the configuration csv file [default: %s]" % input_file)
  parser.add_argument("--lumi", dest="mask", default=ps_column, type=str, action="store", required=False, help="prescale/mask column identifier [default: %s]" % ps_column)
  parser.add_argument("--unprescaled", dest="unprescaled", default=False, action="store_true", required=False, help="use only unprescaled seeds")

  options = parser.parse_args()
  config = csvtool.parse(options.csv, [options.mask,])

  menu_file(config, options)

# end
