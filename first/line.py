

class Line:


    def __init__(self,ident_level:int) -> None:
        self._content = ''
        self._ident_text = ''
        for i in range(0, ident_level):
            self._ident_text += '    '   

    def add_text(self,char:str):
        self._content+=char

