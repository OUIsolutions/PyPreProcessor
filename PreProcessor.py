
from sys import argv
from sys import exit

from typing import Callable
from typing import List
from typing import Any

from json import loads
from json import JSONDecodeError



class ActionResult:

    def __init__(self,text:str,point:int) -> None:
        self._text = text
        self.point = point

    def __str__(self) -> str:
        return self._text
    



class Action:

    def __init__(self,action:Callable,name:str) -> None:
        self.action = action
        self._name = name

    def call(self,callback_args:list):
        return self.action(callback_args)

    def __len__(self):
        return len(self._name)
    
    def __str__(self) -> str:
        return self._name




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

