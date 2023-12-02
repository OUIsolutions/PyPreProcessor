


from src.pre_processor import PreProcessor

p = PreProcessor()
p.args = {'a':10,'x':30}
x = p.amalgamate('target.py')

print(x)