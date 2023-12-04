from shutil import copy 
from os import system
from os import listdir
from os import remove
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
    if not e.endswith('.py'):
        continue

    p = PreProcessor()
    p.internal = False 
    data = {
        'content':p.run(current),
    }
    system(f'python3 {current}')
    with open('before.txt','r') as arq:
        data['before'] = arq.read()

    with open('out.txt','r') as arq:
        data['out'] = arq.read()
    remove('before.txt')
    remove('out.txt')
    main_processor.files[e] = data


readme_result = main_processor.run('templates/README.md')
with open('README.md','w') as arq:
    arq.write(readme_result)
    

  

#system('python3 exemples/sql.py')

