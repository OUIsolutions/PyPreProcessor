
from .line import Line

class TextBlock(Line):


    def __str__(self) -> str:
   
        formated_content  = self._content.replace('\n','\\n');  
        return f'{self._ident_text}self.text+="{self._content}"'