from extras import generate_content_func
class PreProcessor:

    def __init__(self) -> None:
    
        self.identifier = '#comptime:'
        self._text = ''
        
      
    def generate_content_func(self,content:str)->str:
        lines = content.split('\n')
        ident_level = 0
        ident_text = ''
        result =''
        for line in lines:
            if line =='':
                continue
            
            striped_line = line.strip()

            if striped_line.startswith(self.identifier):
                code = striped_line[len(self.identifier):-1]
                result+=f'{code}\n'
        

            result+=f'{ident_text}self.text+="{line}"\n'
        return result



    def input(self,file:str):
        with open(file,'r') as arq:
            content = arq.read()
        converted = self.generate_content_func(content)
        print(converted)


    def compile(self,file:str)->str:
        self.input(file)
        return self._text