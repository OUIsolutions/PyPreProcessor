from extras import create_ident_text
class PreProcessor:

    def __init__(self) -> None:
    
        self.identifier = '#comptime:'
        self.start_scope = 'do'
        self.endscope ='#end'
        self._text = ''
        
      
    def generate_content_func(self,content:str)->str:
        lines = content.split('\n')
        ident_level = 2
        ident_text = create_ident_text(ident_level)
        result =''
        for line in lines:
            if line =='':
                continue
            
            striped_line = line.strip()

            if striped_line.startswith(self.identifier):
                code = striped_line[len(self.identifier)::]

                if code.endswith(self.start_scope):
                    code = code[0:len(code) -len(self.start_scope)]
                    result+=f'{ident_text}{code}\n'
                    ident_level+=1
                    ident_text = create_ident_text(ident_level)
                    continue
                result+=f'{ident_text}{code}\n'
                continue


            if striped_line == self.endscope:
                ident_level-=1
                ident_text = create_ident_text(ident_level)
                continue

            result+=f'{ident_text}self.text+="{line}"\n'
        return result



    def include(self,file:str):
        with open(file,'r') as arq:
            content = arq.read()
        converted = self.generate_content_func(content)
        print(converted)
        
    def compile(self,file:str)->str:
        self.include(file)
        return self._text