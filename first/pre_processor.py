class PreProcessor:

    def __init__(self) -> None:
    
        self.identifier = '#comptime:'
        self.start_scope = ':'
        self.endscope ='#end'
        self.end_comptimes = ['\n','#']
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
        ident_level = 0
        ident_text = ''
        result =''
        inside_comptime = False
        
        for i  in range(0,len(content)):

            if not inside_comptime:
                

                current_char = content[i]
                
                if i > len(content) - len(self.identifier):
                    result+=current_char
                    continue


                possible_identifier = content[i:i+len(self.identifier)]
                is_a_identifier = possible_identifier == self.identifier
       

                if is_a_identifier:
                    inside_comptime = True
                    i+=len(self.identifier)
                    continue


                if not is_a_identifier:
                    result+=current_char


            '''
            #means its equal to comtime
            result+=stage

            instruction_striped = stage.strip()

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
        
        
        result+=stage
        '''
            
        return result



    def include(self,file:str):
        with open(file,'r') as arq:
            content = arq.read()
        converted = self.generate_content_func(content)
        print(converted)

    def compile(self,file:str)->str:
        self.include(file)
        return self._text