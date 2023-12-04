
#comp:if False:
from .line import Line
#end

class TextBlock(Line):


    def __str__(self) -> str:
   
        if self._content == '':
            return ''
        formated_content  = self._content.encode('utf-8')
        return f'{self._ident_text}self._generate({formated_content})'