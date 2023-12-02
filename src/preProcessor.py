from .actions import Action
from typing import List
from typing import Callable

class PreProcessor:

    def __init__(self) -> None:
        self._aready_included = []
        self.include_name = 'include'
        self.ref_name = 'ref'
        self.embed_name ='embed'

    
    def _get_actions(self)->List[Action]:
        return [
            Action(self._include,self.include_name),
            Action(self._ref,self.ref_name),
            Action(self._embed,self.embed_name)
        ]
    
    def _get_action_from_point(self,text:str,point:int)->Action or None:
        actions = self._get_actions()
        for action in actions:
            action:Action

            try:
                possible_action = text[point,point+len(action)]
            except IndexError:
                continue
            if possible_action == str(action):
                return action
            
            
    def _include(self,content:str)->str:
        pass 
    
    def _ref(self,content:str)->str:
        pass 
    
    def _embed(self,content:str)->str:
        pass 




    def amalgamate(self,file:str,args:dict):
        with open(file,'r') as arq:
            content = arq.read()
        content_size = len(content)
        for i in range(0,content_size):
            action = self._get_action_from_point(i,content)
            print(action)

        

        



