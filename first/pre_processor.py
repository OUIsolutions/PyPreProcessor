from action import Action
from action_result import ActionResult
from extras import aply_ident
from typing import List
from typing import Callable
from typing import Any
from json import loads
from .registers import Registers

class PreProcessor:

    def __init__(self) -> None:
        self.args = {}
    
        self.include_name = '#include('
        self.discard_name ='#discard('
        self.end_name = '#end('
        self.ref_name = '#ref('
        self.break_char = ')'
        self._registers = Registers()

    
    
    def _get_actions(self)->List[Action]:
        return [
            Action(self._iNclude,self.include_name),
            Action(self._rEf,self.ref_name),
            Action(self._dIscard,self.discard_name)
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


    def _syscall_tic(self,content:str, content_size:int,started_identation:str):
            
            if self._registers.point >= content_size:
                return False 
            
            
            
            current_char = content[i]
            if current_char == '\n':
                self._registers.acumulated_ident = started_identation
            else:
                self._registers.acumulated_ident+=1
            

            action = self._get_action_from_point(content,i)
            
            action_not_provided = not action
            if action_not_provided and self._registers.operating:
                self._registers.output+=current_char
                self._registers.point+=1
                return True

        
            action_result = self._exec_action(action,content,self._registers.point)

            if action_result and not self._registers.operating:
                raise Exception('you cannot return an text when its not operating')
            
            if action_result:
                self._registers.output+=str(action_result)

            self._registers.point=action_result.point



    def _syscall(self,content:str):
        started_identation = self._registers.acumulated_ident
        content_size = len(content)
        self._registers.point = 0

        while self._syscall_tic(
            content=content,
            started_identation=started_identation,
            content_size=content_size
        ):pass 

        self._registers.acumulated_ident = started_identation 
        self._registers.output+=aply_ident(
                text=self._registers.output,
                ident=self._registers.acumulated_ident
        )
    





    def _dIscard(self,callback_args:list):
        self._registers.operating = False 
    

    def _eNd(self,callback_args:list):
        self._registers.operating =True

    


    def _iNclude(self,callback_args:list)->str:
        try:
            file = callback_args[0]
        except IndexError:
            raise IndexError('file not passed in args ')

        
        with open(file,'r') as arq:
            content = arq.read()

        
        

    def _rEf(self,callback_args:list)->str:
        try:
            arg_to_print = callback_args[0]
        except IndexError:
            raise IndexError('reference not provided')
        
        try:
            value = self.args[arg_to_print]
        except KeyError:
            raise KeyError(f'args {self.args} not have {arg_to_print}')

        
        return str(value)
    



    def _exec_action(self,action:Action,content:str,point:int)->ActionResult:
        
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
        result = action.call(callback_args=formated)
        return ActionResult(text=result,point=i)




    def compile(self,file:str)->str:
        return self._iNclude([file])
        

        


