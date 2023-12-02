


from src.pre_processor import PreProcessor

p = PreProcessor()

x = p.amalgamate('target.py',args={'a':10,'x':30})
print(x)