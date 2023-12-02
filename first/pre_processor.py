class PreProcessor:

    def __init__(self) -> None:
    
        self.identifier = '#comptime:'
        self.start_scope = ':'
        self.endscope ='#end'
        self._text = ''
        #args
        self.t = 20
        self.r= 30
        
    @staticmethod
    def create_ident_text(ident_level:int):    
        ident_text = ''
        for  i in range(0,ident_level):
            ident_text+='    '
        return ident_text

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
                code = striped_line[len(self.identifier)::]
                result+=f'{ident_text}{code}\n'

                if code.endswith(self.start_scope):
                    ident_level+=1
                    ident_text = self.create_ident_text(ident_level)
                    
                continue


            if striped_line == self.endscope:
                ident_level-=1
                ident_text = self.create_ident_text(ident_level)
                continue
            result+=f'{ident_text}self._text+="\\n{line}"\n'
        result+=self.create_ident_text(ident_level)
        return result



    def include(self,file:str):
        with open(file,'r') as arq:
            content = arq.read()
        converted = self.generate_content_func(content)
        exec(converted)

    def compile(self,file:str)->str:
        self.include(file)
        return self._text