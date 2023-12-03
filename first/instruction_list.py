from .text_block import TextBlock
from .code_block import CodeBlock
from typing import List
from typing import Callable

class InstructionList:

    def __init__(self) -> None:
        self._ident_level = 0
        self._instructions:List[TextBlock or CodeBlock] = [
            TextBlock(self._ident_level)
        ]
    


    def increase_ident(self):
        self._ident_level+=1
        last_instruction_constructor:Callable = self._instructions[-1].__class__
        self._instructions.append(last_instruction_constructor(self._ident_level))


    def decrease_ident(self):
        self._ident_level-=1
        last_instruction_constructor:Callable = self._instructions[-1].__class__
        self._instructions.append(last_instruction_constructor(self._ident_level))

    def add_text_to_last_instruction(self,char:str):
        self._instructions[-1].add_text(char)


    def __str__(self) -> str:
        result = ''
        for i in self._instructions:
            result+=str(i) +"\n"
        return result

    def add_text_block(self):
        self._instructions.append(TextBlock(self._ident_level))

 
    def add_code_block(self):
        self._instructions.append(CodeBlock(self._ident_level))
   
