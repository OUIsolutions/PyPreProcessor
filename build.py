from shutil import copy 
from os import system
system('python3 PyPreProcessor.py  src/main.py PyPreProcessor.py ')
copy('PyPreProcessor.py','exemples/PyPreProcessor.py')
system('python3 exemples/sql.py')
