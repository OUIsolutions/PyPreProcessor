
from .line import Line

class CodeBlock(Line):

    def __str__(self) -> str:
        lines = self._content.split('\n')
        lines = list(map(lambda l: l.strip(),lines))
        lines = list(filter(lambda l: l,lines))
        formated_content = ''
        for i in lines:
            formated_content+=f'\n{self._ident_text}{i}' 

        if formated_content == '':
            return ''
        return formated_content