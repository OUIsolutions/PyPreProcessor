from shutil import copy 
from os import system
from os import listdir
from PyPreProcessor import PreProcessor

#boostraping itself 
system('python3 PyPreProcessor.py  main.py PyPreProcessor.py ')

copy('PyPreProcessor.py','internal_exemples/PyPreProcessor.py')

main_processor = PreProcessor()
main_processor.files = {}

exemples = listdir('internal_exemples')
for e in exemples:
    current = f'internal_exemples/{e}'
    if e == 'PyPreProcessor.py':
        continue

    p = PreProcessor()
    p.internal = False 
    data = {
        'file':p.run(current),
    }
    system(f'python3 {current}')
    


  

#system('python3 exemples/sql.py')

