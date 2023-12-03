from .text_block import TextBlock
from .code_block import CodeBlock
from typing import List


class Compiler:

    def __init__(self) -> None:
        self._instructions:List[TextBlock or CodeBlock] = []
    


    def __add__(self,char:str):
        self._instructions[-1].add_char(char)


    def __str__(self) -> str:
        result = ''
        for i in self._instructions:
            result+=str(i) +"\n"
        

    def add_text_block(self):
        self._instructions.append(TextBlock(self._ident_level))


