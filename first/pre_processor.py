from extras import convert_content
class PreProcessor:

    def __init__(self) -> None:
        self.args = {}
        self._text = ''
        
      
    


    def input(self,file:str):
        with open(file,'r') as arq:
            content = arq.read()
        converted = convert_content(content)
        print(converted)


    def compile(self,file:str)->str:
        self.args = {}
        self._text = ''
        self.input(file)
        return self._text