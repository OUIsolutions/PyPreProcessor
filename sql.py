


from PyPreProcessor import PreProcessor


TEMPLATE = 'templates/insert.sql'

#comp: if not self.internal: #>>

OUTPUT = "query.sql"
#<<  

#end 

#comp:if self.internal: #>> #end 
OUTPUT = "out.txt"
#<< 


p = PreProcessor()
p.username = 'Username'
p.email = 'myemail@gamil.com'
p.password = '123'
p.is_root = False

result = p.run(TEMPLATE)
with open(OUTPUT,'w') as arq:
    arq.write(result)


#comp:if self.internal: #>> 
from shutil import copy
copy(TEMPLATE,'before.txt')
#<< #end 

