import base64

y:bytes
#comp:self.embed("teste/screen.png","y")#end

with open('out.png','wb') as arq:
    arq.write(y)