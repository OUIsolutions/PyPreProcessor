from shutil import copy 
from os import system

copy('PyPreProcessor.py','exemples/PyPreProcessor.py')
system('cd exemples')
system('python3 sql.py')
