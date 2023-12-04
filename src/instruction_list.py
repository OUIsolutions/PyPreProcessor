from text_block import TextBlock
from code_block import CodeBlock
from typing import List

class InstructionList:

    def __init__(self) -> None:
        self._ident_level = 0
        self._instructions:List[TextBlock or CodeBlock] = [
            TextBlock(self._ident_level)
        ]
    

    def increase_code_ident(self):
        self._ident_level+=1
  

    def decrease_code_ident(self):
        self._ident_level-=1


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
   
