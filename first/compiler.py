from .text_block import TextBlock
from .code_block import CodeBlock
from typing import List


class Compiler:

    def __init__(self) -> None:
        self._ident_level = 0
        self._instructions:List[TextBlock or CodeBlock] = []
    


    def increase_ident(self):
        self._ident_level+=1
    
    def decrease_ident(self):
        self._ident_level-=1


    def __add__(self,char:str):
        self._instructions[-1]+=char


    def __str__(self) -> str:
        result = ''
        for i in self._instructions:
            result+=str(i) +"\n"
        

    def add_text_block(self):
        self._instructions.append(TextBlock(self._ident_level))

    
