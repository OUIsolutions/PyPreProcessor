from .TextBlock import TextBlock

from typing import List


class Compiler:

    def __init__(self) -> None:
        self.instructions:List[TextBlock] = []
    
    def add_char(self,char:str):
        self.instructions[-1].content+=char


