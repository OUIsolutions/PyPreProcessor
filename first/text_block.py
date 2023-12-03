
#comp:if False:
from .line import Line
#end

class TextBlock(Line):


    def __str__(self) -> str:
   
        formated_content  = self._content.replace('\n','\\n');  
        return f'{self._ident_text}self.text+="{formated_content}"'