from typing import List
from .instruction_list import InstructionList

class PreProcessor:

    def __init__(self) -> None:

        self.identifier = '#comp:'
        self.start_scope = ':'
        self.endscope = '#end'
        self.end_comptimes = ['\n','#']
        self._text = ''
        self._instructions:InstructionList = None
        self._point:int  = None
        self._content:str = None 
        self._inside_comptime:bool = None
        self._current_char:str = None
        # args
        self.t = 20
        self.r = 30


    def is_string_from_point(self, content: str, point: int, expected: str):
        try:
            comparation = content[point:point + len(expected)]
            return comparation == expected
        except IndexError:
            return False

    def get_expected_if_is_one_of_expecteds(self, content: str, point: int, expecteds: List[str]):
        for i in expecteds:
            if self.is_string_from_point(content, point, i):
                return i
        return None


    def handler_comptime_text(self)->bool:

        INCREASE_AND_ADD_CURRENT_CHAR = True 
        NOT_MOVE_CHAR = False 
        end_char = self.get_expected_if_is_one_of_expecteds(self._content, self._point, self.end_comptimes)
        is_an_end_comptime:bool = end_char != None
        
        #means its \n or  # on end of comptime
        if is_an_end_comptime:
            self._instructions.add_text_block()
            self._inside_comptime = False
            self._point += len(end_char)
            return NOT_MOVE_CHAR 
        
        #means its : char
        is_start_scope = self.is_string_from_point(self._content, self._point, self.start_scope)
        if is_start_scope:
            self._instructions.add_text_to_last_instruction(self._current_char)
            self._instructions.increase_ident()
            self._point+=1
            return NOT_MOVE_CHAR
        
        return INCREASE_AND_ADD_CURRENT_CHAR 



    def handler_normal_text(self)->bool:
        INCREASE_AND_ADD_CURRENT_CHAR = True 
        NOT_MOVE_CHAR = False 

        is_start_comptime_identfier =self.is_string_from_point(self._content, self._point, self.identifier)
    
        if is_start_comptime_identfier:
            self._instructions.add_code_block()
            self._inside_comptime = True
            self._point += len(self.identifier)
            return NOT_MOVE_CHAR 
        
        return INCREASE_AND_ADD_CURRENT_CHAR 
        

    def compile(self, content: str) -> str:
     
        self._instructions  = InstructionList()
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

        
            add_char_and_increase_point =  True 
            is_a_normal_text = not self._inside_comptime
            if is_a_normal_text:
              add_char_and_increase_point = self.handler_normal_text()
                
            
            if self._inside_comptime:
               add_char_and_increase_point = self.handler_comptime_text()

            if add_char_and_increase_point:
                self._instructions.add_text_to_last_instruction(self._current_char)
                self._point+=1

    


    def include(self, file: str):
        with open(file, 'r') as arq:
            content = arq.read()
        converted = self.compile(content)
        print(converted)

    def run(self, file: str) -> str:
        self.include(file)
        return self._text
