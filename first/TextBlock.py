
class TextBlock:

    def __init__(self,ident_level:int) -> None:
        self._content = ''
        self._ident_level = ident_level


    def add_char(self,char:str):
        self._content+=char



    def __str__(self) -> str:
        ident_text = ''
        for i in range(0, self._ident_level):
            ident_text += '    '      
        formated_content  = self._content.replace('\n','\\n');  
        return f'{ident_text}self.text+="{self.content}"'