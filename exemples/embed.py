


from PyPreProcessor import PreProcessor


TEMPLATE = 'templates/embed.py'

 
OUTPUT = "embed.py"
  

p = PreProcessor()


result = p.run(TEMPLATE)
with open(OUTPUT,'w') as arq:
    arq.write(result)

 

