
#comp: if False: #>>  #end
from typing import List
from typing import Any
from instruction_list import InstructionList
from extras import aply_ident
from traceback import format_exc
from compiler_props import CompilerProps 
#<< 



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

        is_an_end_comptime =self.is_string_from_point(self._content, self._point, self.end_comptime)
        
        if is_an_end_comptime:
            compiler_props._instructions.add_text_block()
            self._inside_comptime = False
            compiler_props._point += len(self.end_comptime)
            return  
        
        is_start_scope = self.is_string_from_point(self._content, self._point, self.start_scope)
        if is_start_scope:
            compiler_props._instructions.increase_code_ident()
            compiler_props._point+=len(self.start_scope)
            return 
        
        compiler_props._instructions.add_text_to_last_instruction(self._current_char)
        compiler_props._point+=1



    def handler_normal_text(self,compiler_props:CompilerProps)->bool:
            
        if compiler_props._current_char == '\n':
            self._normal_text_ident =self._previews_file_text_ident

        if compiler_props._current_char == ' ':
            self._normal_text_ident+=1


        is_start_comptime_identfier =self.is_string_from_point(self._content, self._point, self.start_comptime)
    
        if is_start_comptime_identfier:
            compiler_props._instructions.add_code_block(self._normal_text_ident)
            self._inside_comptime = True
            compiler_props._point += len(self.start_comptime)
            return  
        

        compiler_props._instructions.add_text_to_last_instruction(self._current_char)
        compiler_props._point+=1

        

    def compile(self) -> str:
     
        compiler_props = CompilerProps()

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
