
Codigo

~~~python
#comp:
content =self.files["sql.py"]["content"] 
self.ref(content)
#end
~~~
Antes
~~~sql
#comp:
content =self.files["sql.py"]["before"] 
self.ref(content)
#end
~~~
Saida
~~~sql
#comp:
content =self.files["sql.py"]["out"] 
self.ref(content)
#end
~~~
