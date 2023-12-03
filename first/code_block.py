
from .line import Line

class CodeBlock(Line):

    def __str__(self) -> str:
        lines = self._content.split('\n')
        lines = list(map(lambda l: l.strip(),lines))
        formated_conent = '\n'.join(lines)

        if formated_conent == '':
            return ''
        return f'{self._ident_text}{formated_conent}'