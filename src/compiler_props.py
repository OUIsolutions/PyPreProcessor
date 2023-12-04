#comp: if False: #>>
from .instruction_list import InstructionList
#<< #end


class CompilerProps:
        
    def __init__(self) -> None:
        self._instructions = InstructionList()
        self._point = 0
        self._content:str =''
        self._current_char:str  = ''
