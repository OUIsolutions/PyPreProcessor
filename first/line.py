

class Line:


    def __init__(self,ident_level:int) -> None:
        self._content = ''
        self._ident_text = ''
        for i in range(0, self.ident_level):
            self._ident_text += '    '   

    def __add__(self,char:str):
        self._content+=char

