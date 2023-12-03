
class TextBlock:

    def __init__(self,ident_level:int) -> None:
        self.content = ''
        self.ident_level = ident_level


    def __str__(self) -> str:
        ident_text = ''
        for i in range(0, ident_text):
            ident_text += '    '      
        formated_content  = self.content.replace('\n','\\n');  
        return f'{ident_text}self.text+="{self.content}"'