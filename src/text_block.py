
#comp:if False:
from line import Line
from extras import aply_ident
#end

class TextBlock(Line):

    def __init__(self, ident_level: int) -> None:
        super().__init__(ident_level)

    def __str__(self) -> str:
   
        if self._content == '':
            return ''
        formated_content  = self._content.encode('utf-8')
        return f'{self._ident_text}self._generate({formated_content})'