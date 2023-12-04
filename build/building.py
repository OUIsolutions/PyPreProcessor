


from PyPreProcessor import PreProcessor


TEMPLATE = 'templates/index.html'

#comp: if not self.internal: #>>#end 
OUTPUT = "ambient.py"
#<<  


#comp:if self.internal: #>> #end 
OUTPUT = "out.txt"
#<< 


p = PreProcessor()



result = p.run(TEMPLATE)
with open(OUTPUT,'w') as arq:
    arq.write(result)

#comp:if self.internal: #>> 
from shutil import copy
copy(TEMPLATE,'before.txt')
#<< #end 

