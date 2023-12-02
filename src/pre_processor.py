from .action import Action
from .action_result import ActionResult
from typing import List
from typing import Callable
from json import loads


class PreProcessor:

    def __init__(self) -> None:
        self._aready_included = []
        self.include_name = 'include('
        self.ref_name = 'ref('
        self.embed_name ='embed('
        self.break_char = ')'
    
    def _get_actions(self)->List[Action]:
        return [
            Action(self._include,self.include_name),
            Action(self._ref,self.ref_name),
            Action(self._embed,self.embed_name)
        ]
    

    def _get_action_from_point(self,text:str,start_point:int)->Action or None:
        actions = self._get_actions()
        for action in actions:
            action:Action

            try:
                end_point = start_point + len(action)
                possible_action = text[start_point:end_point]
            except IndexError:
                continue
            if possible_action == str(action):
                return action
            



    def _include(self,callback_args:list,args:dict)->str:
        return 'nada'
        
    
    def _ref(self,callback_args:list,args:dict)->str:
        return 'nada'
        pass 
    
    def _embed(self,callback_args:list,args:dict)->str:
        return 'nada'


    def _exec_action(self,action:Action,content:str,point:int,args:dict)->ActionResult:
        
        start_point = point+len(action)
        content_size = len(content)
        args_string = '['
        i = start_point
        while True:
            current_char = content[i]
            i+=1
            if current_char == self.break_char:
                break
            if current_char == "'":
                args_string+='"'
                continue
            args_string+=current_char
           
            
        args_string+=']'
        formated = loads(args_string)
        result = action.call(formated,args)
        return ActionResult(result,i)


    def amalgamate(self,file:str,args:dict={})->str:
        
        result = ''
        with open(file,'r') as arq:
            content = arq.read()
        content_size = len(content)
        i = 0
        while True:
            
            
            action = self._get_action_from_point(content,i)
            
            if not action:
                current_char = content[i]
                result+=current_char
                continue
            
            action_result = self._exec_action(action,content,i,args)
            
            i = action_result.point
            
            if i == content_size:
                break
         


        return result
        

        



