from shutil import copy 
from os import system
from os import listdir
from os import remove
from os import makedirs
from shutil import rmtree
from PyPreProcessor import PreProcessor
rmtree('exemples')
makedirs('exemples')

#boostraping itself 
system('python3 PyPreProcessor.py  main.py PyPreProcessor.py ')

copy('PyPreProcessor.py','build/PyPreProcessor.py')

main_processor = PreProcessor()
main_processor.files = {}

exemples = listdir('build')
for e in exemples:
    current = f'build/{e}'
    if e == 'PyPreProcessor.py':
        continue
    if not e.endswith('.py'):
        continue

    p = PreProcessor()
    p.internal = False 
    result = p.run(current)
    data = {
        'content':result,
    }

    with open(f'exemples/{e}' ,'w') as arq:
        arq.write(result)


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

