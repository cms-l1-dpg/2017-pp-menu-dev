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
# L1Seed                                                     Bit  Prescale POG     PAG 
'''

  output = file('menu.txt', 'w')
  output.write(header)
  for idx, name in config.algorithms.iteritems():
    output.write('{:60} {:>3}         {}\n'.format(name, idx, config.masks[idx] if idx in config.masks else 0))
  output.close()

  return


if __name__ == '__main__':
  config = csvtool.parse(input_file)

  menu_file(config)

# end
