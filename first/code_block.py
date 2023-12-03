
from .line import Line

class CodeBlock(Line):

    def __str__(self) -> str:
        formated_conent = self._content.strip()

        if formated_conent == '':
            return ''
        return f'{self._ident_text}{formated_conent}'