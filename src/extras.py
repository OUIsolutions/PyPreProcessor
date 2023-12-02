


def aply_ident(text:str,ident:int):
    if ident == 0:
        return text
    
    ident_text = ''
    for  i in range(0,ident):
        ident_text+=' '
    
    lines = text.split('\n')
    result = ''
    for line in lines:
        result+=ident_text+line
    return result
