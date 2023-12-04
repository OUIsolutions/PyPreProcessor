
#comp:if False:
from .line import Line
from .extras import aply_ident
#end

class TextBlock(Line):

    def __init__(self, ident_level: int,normal_text_ident:int) -> None:
        super().__init__(ident_level)
        self._normal_text_ident = normal_text_ident

    def __str__(self) -> str:
   
        if self._content == '':
            return ''
        formated_content = aply_ident(self._content,self._normal_text_ident)
        formated_content  = formated_content.encode('utf-8')
        return f'{self._ident_text}self._generate({formated_content})'