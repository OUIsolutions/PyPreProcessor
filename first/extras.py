


def aply_ident(text:str,ident:int):
    if ident == 0:
        return text
    
    ident_text = '\n'
    for  i in range(0,ident-1):
        ident_text+=' '
    
    lines = text.split('\n')
    result = ''
    for line in lines:
        result+=ident_text+line
    return result



def create_ident_text(ident_level:int):    
    ident_text = ''
    for  i in range(0,ident_level):
        ident_text+='    '
    return ident_text

    

def generate_content_func(content:str)->str:
    lines = content.split('\n')
    ident_level = 0
    ident_text = ''
    result =''
    IDENTIFIER = '#comptime:'
    for line in lines:
        if line =='':
            continue
        
        striped_line = line.strip()

        if striped_line.startswith(IDENTIFIER):
            code = striped_line[len(IDENTIFIER):-1]
            result+=f'{code}\n'
    

        result+=f'{ident_text}self.text+="{line}"\n'
    return result
