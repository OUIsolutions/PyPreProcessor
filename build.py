from shutil import copy 
from os import system
from os import listdir
from PyPreProcessor import PreProcessor

system('python3 PyPreProcessor.py  main.py PyPreProcessor.py ')

copy('PyPreProcessor.py','internal_exemples/PyPreProcessor.py')

main_processor = PreProcessor()

exemples = listdir('internal_exemples')
for e in exemples:
    current = f'internal_exemples/{e}'
    p = PreProcessor()
    p.internal = True 
    data = {
        'file':p.run(current),
    }
    p.internal = False 
    code_to_execute = p.run(current)
    print(code_to_execute)
    
    
  

system('python3 exemples/sql.py')

