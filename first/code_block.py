
from .line import Line

class CodeBlock(Line):

    def __str__(self) -> str:
           return f'{self._ident_text}{self._content}'