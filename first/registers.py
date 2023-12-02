
from typing import Callable
class Registers:

    
    def __init__(self) -> None:
        #self.acumulated_ident = 0

        self.jump = 0
        self.point = 0

        self.stage = ''
        self.callback_action:Callable = None
        self.args =[

            
        ]


        self.compilation_result =''

        #stores the code of the program
        self.code = ''
        self.code_size = 0

