
Codigo

~~~python



from PyPreProcessor import PreProcessor


TEMPLATE = 'templates/insert.sql'

 


 

p = PreProcessor()
p.username = 'Username'
p.email = 'myemail@gamil.com'
p.password = '123'
p.is_root = False

result = p.run(TEMPLATE)
with open(OUTPUT,'w') as arq:
    arq.write(result)


 


~~~


Antes
~~~sql



INSERT INTO #comp: 
    if self.is_root: #>> 
        self.ref('root')
    #<<
    if not self.is_root: #>> 
        self.ref('users')
    #<<
    #end (username, email, password) 
VALUES (
        '#comp: self.ref(self.username) #end', 
        '#comp: self.ref(self.email) #end',
        '#comp: self.ref(self.password) #end'
);

~~~


Saida
~~~sql



INSERT INTO users (username, email, password) 
VALUES (
        'Username', 
        'myemail@gamil.com',
        '123'
);

~~~
