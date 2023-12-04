

#if self.internal: >> 
TEMPLATE_FOLDER = '../templates'
OUTPUT = "out.txt"
#end 

#if not self.internal: >> 
TEMPLATE_FOLDER = 'templates'
OUTPUT = "query.sql"
#end 




