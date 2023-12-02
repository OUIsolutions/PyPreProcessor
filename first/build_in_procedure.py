from typing import Callable

class BuildInProcedure:

    def __init__(self,action:Callable,name:str,simple_scope_open:bool =False,end_scope:bool=False) -> None:
        self.action = action
        self._name = name
        self.simple_scope_open = simple_scope_open
        self.end_scope = end_scope
    
    

    def call(self,callback_args:list):
        return self.action(callback_args)

    def __len__(self):
        return len(self._name)
    
    def __str__(self) -> str:
        return self._name