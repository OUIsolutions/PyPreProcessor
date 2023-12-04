

from typing import List
from typing import Any
from instruction_list import InstructionList
from extras import aply_ident

class PreProcessor:

    def __init__(self) -> None:

        #these is for allowing bootstraping process
        self.start_comptime = '#comp$:'.replace('$','')
        self.start_scope = '#>$>'.replace('$','')
        self.endscope = '#<$<'.replace('$','')
        self.end_comptime = '#en$d'.replace('$','')
        

        
        self._resset_state()
        # args
        self.t = 20
        self.r = 20
        self.a = '"#comp: self.aaaaaaaaa #end'
        self.lista = [1,2,3]


    def _resset_state(self):
        self._text = ''
        self._instructions = InstructionList()
        self._point = 0
        self._content:str =''
        self._inside_comptime = False
        self._current_char:str  = ''
        #these is the ident of the text, not the comptime text
        self._normal_text_ident = 0 
        self._previews_file_text_ident = 0

    def is_string_from_point(self, content: str, point: int, expected: str):
        try:
            comparation = content[point:point + len(expected)]
            return comparation == expected
        except IndexError:
            return False



    def handler_comptime_text(self)->bool:

        is_an_end_comptime =self.is_string_from_point(self._content, self._point, self.end_comptime)
        
        if is_an_end_comptime:
            self._instructions.add_text_block()
            self._inside_comptime = False
            self._point += len(self.end_comptime)
            return  
        
        is_start_scope = self.is_string_from_point(self._content, self._point, self.start_scope)
        if is_start_scope:
            self._instructions.increase_code_ident()
            self._point+=len(self.start_scope)
            return 
        
        self._instructions.add_text_to_last_instruction(self._current_char)
        self._point+=1



    def handler_normal_text(self)->bool:
            
        if self._current_char == '\n':
            self._normal_text_ident =self._previews_file_text_ident

        if self._current_char == ' ':
            self._normal_text_ident+=1


        is_start_comptime_identfier =self.is_string_from_point(self._content, self._point, self.start_comptime)
    
        if is_start_comptime_identfier:
            self._instructions.add_code_block(self._normal_text_ident)
            self._inside_comptime = True
            self._point += len(self.start_comptime)+1
            return  
        

        self._instructions.add_text_to_last_instruction(self._current_char)
        self._point+=1

        

    def compile(self) -> str:
     
        self._instructions = InstructionList()
        self._point = 0
        self._inside_comptime = False
        self._current_char:str  = ''


        while True:
            if self._point >= len(self._content):
                return str(self._instructions)



            self._current_char = self._content[self._point]

            
            is_the_end_scope = self.is_string_from_point(self._content, self._point, self.endscope)
            if is_the_end_scope:
                self._point+=len(self.endscope)
                self._instructions.decrease_code_ident()
                continue

            is_a_normal_text = not self._inside_comptime
            

            if is_a_normal_text:
              self.handler_normal_text()
              continue  
            
            if self._inside_comptime:
               self.handler_comptime_text()
               continue  


    
    def ref(self,element:Any):
        self._text+=str(element)


    def _generate(self,text:bytes):
        self._text+=text.decode('utf-8')

    def exec(self,content:str):
        self._content = content
        converted = self.compile()
        self._inside_comptime = False  
        exec(converted)
        


    def include(self, file: str):       
        self._previews_file_text_ident = self._normal_text_ident
        self._target_file = file
        
        with open(file, 'r') as arq:
             content = arq.read()
        formated_content = aply_ident(content,self._normal_text_ident)
        try:     
            self.exec(formated_content)
        except Exception as e:
            print(formated_content)
            raise e


    def run(self, file: str) -> str:
        self._resset_state()
        self.include(file)
        return self._text
