


from PyPreProcessor import PreProcessor


TEMPLATE = 'templates/index.html'

#comp: if not self.internal: #>>#end 
OUTPUT = "index.html"
#<<  


#comp:if self.internal: #>> #end 
OUTPUT = "out.txt"
#<< 


p = PreProcessor()
p.users =[
    {"name":"test1","age":25,"married":False},
    {"name":"test2","age":26,"married":False},
    {"name":"test3","age":27,"married":False},
    {"name":"test4","age":27,"married":False}

]


result = p.run(TEMPLATE)
with open(OUTPUT,'w') as arq:
    arq.write(result)

#comp:if self.internal: #>> 
from shutil import copy
copy(TEMPLATE,'before.txt')
#<< #end 
