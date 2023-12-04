


from typing import List
from typing import Any
from json import loads
from json import JSONDecodeError
from sys import argv
from sys import exit
import traceback
from typing import List
from typing import Callable











def aply_ident(text:str,ident:int):
    if ident == 0:
        return text
    
    ident_text = '\n'
    for  i in range(0,ident-1):
        ident_text+=' '
    
    lines = text.split('\n')
    result = ''
    for line in lines:
        result+=ident_text+line
    return result





 


class Line:


    def __init__(self,ident_level:int) -> None:
        self._content = ''
        self._ident_text = ''
        for i in range(0, ident_level):
            self._ident_text += '    '   

    def add_text(self,char:str):
        self._content+=char

 









class CodeBlock(Line):

    def __str__(self) -> str:
        lines = self._content.split('\n')
        lines = list(map(lambda l: l.strip(),lines))
        lines = list(filter(lambda l: l,lines))
        formated_content = ''
        for i in lines:
            formated_content+=f'\n{self._ident_text}{i}' 

        if formated_content == '':
            return ''
        return formated_content 


 


class TextBlock(Line):

    def __init__(self, ident_level: int) -> None:
        super().__init__(ident_level)

    def __str__(self) -> str:
   
        if self._content == '':
            return ''
        formated_content  = self._content.encode('utf-8')
        return f'{self._ident_text}self._generate({formated_content})' 


 

class InstructionList:

    def __init__(self) -> None:
        self._ident_level = 0
        self._instructions:List[TextBlock or CodeBlock] = [
            TextBlock(self._ident_level)
        ]
    

    def increase_code_ident(self):
        self._ident_level+=1
        constructor = self._instructions[-1].__class__
        generated = constructor(self._ident_level)
        self._instructions.append(generated)

        
  

    def decrease_code_ident(self):
        self._ident_level-=1
        constructor = self._instructions[-1].__class__
        generated = constructor(self._ident_level)
        self._instructions.append(generated)
        
    def add_text_to_last_instruction(self,char:str):
        self._instructions[-1].add_text(char)

    

    def __str__(self) -> str:
        result = ''
        for i in self._instructions:
            generated = str(i)
            if not generated:
                continue
            result+=str(i) +"\n"
        return result

    def add_text_block(self):
        self._instructions.append(TextBlock(self._ident_level))

 
    def add_code_block(self,normal_text_ident:int):
        block  = CodeBlock(self._ident_level)
        block.add_text(f'self._normal_text_ident = {normal_text_ident}\n')
        self._instructions.append(block)
   
 

 



class PreProcessor:

    def __init__(self) -> None:

        #these is for allowing bootstraping process
        self.start_comptime = '#comp$:'.replace('$','')
        self.start_scope = '#>$>'.replace('$','')
        self.endscope = '#<$<'.replace('$','')
        self.end_comptime = '#en$d'.replace('$','')        
        self._resset_props()
    


    def _resset_props(self):
        #these is the ident of the text, not the comptime text
        self._normal_text_ident = 0 
        self._previews_file_text_ident = 0
        self._inside_comptime = False
        self._text = ''

    def is_string_from_point(self, content: str, point: int, expected: str):
        try:
            comparation = content[point:point + len(expected)]
            return comparation == expected
        except IndexError:
            return False



    def handler_comptime_text(self,compiler_props:CompilerProps)->bool:

        is_an_end_comptime =self.is_string_from_point(self._content, compiler_props._point, self.end_comptime)
        
        if is_an_end_comptime:
            compiler_props._instructions.add_text_block()
            self._inside_comptime = False
            compiler_props._point += len(self.end_comptime)
            return  
        
        is_start_scope = self.is_string_from_point(self._content, compiler_props._point, self.start_scope)
        if is_start_scope:
            compiler_props._instructions.increase_code_ident()
            compiler_props._point+=len(self.start_scope)
            return 
        
        compiler_props._instructions.add_text_to_last_instruction(compiler_props._current_char)
        compiler_props._point+=1



    def handler_normal_text(self,compiler_props:CompilerProps)->bool:
            
        if compiler_props._current_char == '\n':
            self._normal_text_ident =self._previews_file_text_ident

        if compiler_props._current_char == ' ':
            self._normal_text_ident+=1


        is_start_comptime_identfier =self.is_string_from_point(self._content, compiler_props._point, self.start_comptime)
    
        if is_start_comptime_identfier:
            compiler_props._instructions.add_code_block(self._normal_text_ident)
            self._inside_comptime = True
            compiler_props._point += len(self.start_comptime)
            return  
        

        compiler_props._instructions.add_text_to_last_instruction(compiler_props._current_char)
        compiler_props._point+=1

        

    def compile(self) -> str:
     
        compiler_props = CompilerProps()
        compiler_props._content = self._content
        while True:
            if compiler_props._point >= len(compiler_props._content):

                return str(compiler_props._instructions)

            compiler_props._current_char = compiler_props._content[compiler_props._point]
            
            is_the_end_scope = self.is_string_from_point(
                compiler_props._content, 
                compiler_props._point, 
                self.endscope
                )
            
            if is_the_end_scope:
                compiler_props._point+=len(self.endscope)
                compiler_props._instructions.decrease_code_ident()
                continue

            is_a_normal_text = not self._inside_comptime
            

            if is_a_normal_text:
              self.handler_normal_text(compiler_props)
              continue  
            
            if self._inside_comptime:
               self.handler_comptime_text(compiler_props)
               continue  


    
    def ref(self,element:Any):
        self._text+=str(element)


    def _generate(self,text:bytes):
        self._text+=text.decode('utf-8')

    def exec(self,content:str):
        self._content = content
        converted = self.compile()
        #print(converted)
        self._inside_comptime = False  
        try:
            exec(converted)
        except Exception as e:
            print(converted)
            print('==================================================')  
            print(format_exc(e))   
            raise e 
        
        
    def include(self, file: str):       
        self._previews_file_text_ident = self._normal_text_ident
        self._target_file = file
        
        with open(file, 'r') as arq:
             content = arq.read()
        formated_content = aply_ident(content,self._normal_text_ident)
    
        self.exec(formated_content)
 

    def run(self, file: str) -> str:
        self._resset_props()
        self.include(file)
        return self._text
 





def main():
    try:
        target = argv[1]
    except IndexError:
        print('target of compilation not provided')
        exit(1)
    try:
        output = argv[2]
    except IndexError:
        print('output not provided ')
        exit(1)
    
    args = None
    try:
        args = argv[3]
    except IndexError:
        pass 

    preprocessor = PreProcessor()
    if args:
        try:
            converted_args = loads(args)
        except JSONDecodeError as e:
            print(e)
            exit(1)
        for key in args:
            value = args[key]
            preprocessor.__setattr__(value)
    try:
        result = preprocessor.run(target)
    except Exception as e:
        print(traceback.format_exc())
        exit(1)
    
        
    
    with open(output,'w') as arq:
        arq.write(result)


    


if __name__ == '__main__':
    main()