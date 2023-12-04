


from PyPreProcessor import PreProcessor


TEMPLATE = 'templates/insert.sql'

 
OUTPUT = "query.sql"
  


 


p = PreProcessor()
p.username = 'Username'
p.email = 'myemail@gamil.com'
p.password = '123'
p.is_root = False

result = p.run(TEMPLATE)
with open(OUTPUT,'w') as arq:
    arq.write(result)


 

