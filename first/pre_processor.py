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


    def is_string_from_point(self,content:str,point:int,expected:str):
        try:
            comparation = content[point:point+len(expected)]
            return comparation == expected
        except IndexError:
            return False
          

    def generate_content_func(self,content:str)->str:
        ident_level = 0
        ident_text = ''
        result ='self.text+="'
        inside_comptime = False
        for i  in range(0,len(content)):
            current_char = content[i]

            if not inside_comptime:
                
                if self.is_string_from_point(content,i,self.identifier):
                    result+='"'
                    inside_comptime = True
                    i+=len(self.identifier)
                    continue

                result+=current_char.replace("\n","\\n")
                continue

                            
                #print(instruction)
                

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