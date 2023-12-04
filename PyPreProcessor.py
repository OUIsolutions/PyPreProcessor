
from json import loads
from json import JSONDecodeError
from sys import argv
from sys import exit
import traceback


#internal files will be referenced by include


class Line:


    def __init__(self,ident_level:int) -> None:
        self._content = ''
        self._ident_text = ''
        for i in range(0, ident_level):
            self._ident_text += '    '   

    def add_text(self,char:str):
        self._content+=char

 

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





def main():
    try:
        target = argv[1]
    except IndexError:
        print('target of compilation not provided')
        exit(1)
    try:
        output = argv[2]
    except IndexError:
        print('output not provided ')
        exit(1)
    
    args = None
    try:
        args = argv[3]
    except IndexError:
        pass 

    preprocessor = PreProcessor()
    if args:
        try:
            converted_args = loads(args)
        except JSONDecodeError as e:
            print(e)
            exit(1)
        for key in args:
            value = args[key]
            preprocessor.__setattr__(value)
    try:
        result = preprocessor.run(target)
    except Exception as e:
        print(traceback.format_exc())
        exit(1)
    
        
    
    with open(output,'w') as arq:
        arq.write(result)


    


if __name__ == '__main__':
    main()