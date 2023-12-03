
from .line import Line

class CodeBlock(Line):

    def __str__(self) -> str:
        if self._content == '':
            return ''
        return f'{self._ident_text}{self._content}'