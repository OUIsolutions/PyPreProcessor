from shutil import copy 
from os import system
system('python3 PyPreProcessor.py  main.py PyPreProcessor.py ')
copy('PyPreProcessor.py','internal_exemples/PyPreProcessor.py')

from PyPreProcessor import PreProcessor

p = PreProcessor()

system('python3 exemples/sql.py')

