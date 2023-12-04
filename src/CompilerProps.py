#comp: if False: #>>
from instruction_list import InstructionList
#<< #end


class CompilerProps:
        
    def __init__(self) -> None:
        self._text = ''
        self._instructions = InstructionList()
        self._point = 0
        self._content:str =''
        self._inside_comptime = False
        self._current_char:str  = ''
        #these is the ident of the text, not the comptime text
        self._normal_text_ident = 0 
        self._previews_file_text_ident = 0