from src import PreProcessor


p = PreProcessor()
p.internal = False
r = p.run('sql.py')
print(r)