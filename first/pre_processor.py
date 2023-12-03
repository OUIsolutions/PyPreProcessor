from typing import List
from typing import Any
from .instruction_list import InstructionList

class PreProcessor:

    def __init__(self) -> None:

        self.start_comptime = '#comp:'
        self.start_scope = '#>>'
        self.endscope = '#<<'
        self.end_comptime = '#end'
        self._text = ''
        self._instructions:InstructionList = None
        self._point:int  = None
        self._content:str = None 
        self._inside_comptime:bool = None
        self._current_char:str = None
        # args
        self.t = 20
        self.r = 20
        self.a = "funcionou"

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
            self._instructions.increase_ident()
            self._point+=len(self.start_scope)
            return 
        
        self._instructions.add_text_to_last_instruction(self._current_char)
        self._point+=1



    def handler_normal_text(self)->bool:

        is_start_comptime_identfier =self.is_string_from_point(self._content, self._point, self.start_comptime)
    
        if is_start_comptime_identfier:
            self._instructions.add_code_block()
            self._inside_comptime = True
            self._point += len(self.start_comptime)+1
            return  
        

        self._instructions.add_text_to_last_instruction(self._current_char)
        self._point+=1

        

    def compile(self, content: str,ident_level:int=0) -> str:
     
        self._instructions  = InstructionList(ident_level)
        self._point = 0
        self._content =content
        self._inside_comptime = False
        self._current_char = ''
        while True:
            if self._point >= len(self._content):
                return str(self._instructions)

            self._current_char = self._content[self._point]

            is_the_end_scope = self.is_string_from_point(self._content, self._point, self.endscope)
            if is_the_end_scope:
                self._point+=len(self.endscope)
                self._instructions.decrease_ident()
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

    def include(self, file: str):
        with open(file, 'r') as arq:
            content = arq.read()

        converted = self.compile(content)
        self._inside_comptime = False
        exec(converted)


    def run(self, file: str) -> str:
        self.include(file)
        return self._text
