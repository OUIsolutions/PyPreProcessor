
from typing import Callable
class Registers:

    
    def __init__(self) -> None:
        #self.acumulated_ident = 0

        self.jump = 0
        self.point = 0
        self.stage = ''
        self.compilation_result =''

        #stores the code of the program
        self.code = ''
        self.code_size = 0


    def resset_stage(self):
        self.stage = ''

    def get_current_char(self):
        return self.code[self.point]
  
    def add_last_char_to_stage(self):
        self.stage+=self.get_current_char()

    def next(self):
        self.point+=1
        return True