from typing import Callable

class Action:

    def __init__(self,action:Callable,name:str) -> None:
        self.action = action
        self._name = name

    def __len__(self):
        return len(self._name)
    
    def __str__(self) -> str:
        return self._name