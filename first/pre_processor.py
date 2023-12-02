from first.build_in_procedure import BuildInProcedure
from extras import aply_ident
from typing import List
from typing import Callable
from typing import Any
from json import loads
from .cpu import Cpu

class PreProcessor:

    def __init__(self) -> None:
        self.args = {}
    
        self.include_name = '#include('
        self.discard_name ='#discard('
        self.end_name = '#end('
        self.ref_name = '#ref('
        self.break_char = ')'
        self._cpu = Cpu()

    
    
    def _get_procedure(self)->List[BuildInProcedure]:
        return [
            BuildInProcedure(self._iNclude,self.include_name),
            BuildInProcedure(self._rEf,self.ref_name),
            BuildInProcedure(self._dIscard,self.discard_name,simple_scope_open=True),
            BuildInProcedure(self._eNd,self.end_name,end_scope=True)
        ]
    

    def _get_action_from_point(self,text:str,start_point:int)->BuildInProcedure or None:
        procedures = self._get_procedure()
        for proc in procedures:
            proc:BuildInProcedure

            try:
                end_point = start_point + len(proc)
                possible_call = text[start_point:end_point]
            except IndexError:
                continue
            if possible_call == str(proc):
                return proc


    def _syscall_tic(self,content:str, content_size:int,started_identation:str):
            
            if self._cpu.point >= content_size:
                return False 
            
            
            current_char = content[i]
            if current_char == '\n':
                self._cpu.acumulated_ident = started_identation
            else:
                self._cpu.acumulated_ident+=1
            

            action = self._get_action_from_point(content,self._cpu.point)
            
            action_not_provided = not action
            if action_not_provided and self._cpu.operating:
                self._cpu.output+=current_char
                self._cpu.point+=1
                return True

        
            action_result = self._exec_procedure(action,content,self._cpu.point)

            if str(action_result) and not self._cpu.operating:
                raise Exception('you cannot return an text when its not operating')
            
            
            if action_result:
                self._cpu.output+=str(action_result)

            self._cpu.point=action_result.point



    def _syscall(self,content:str):
        started_identation = self._cpu.acumulated_ident
        content_size = len(content)
        self._cpu.point = 0

        while self._syscall_tic(
            content=content,
            started_identation=started_identation,
            content_size=content_size
        ):pass 

        self._cpu.acumulated_ident = started_identation 
        self._cpu.output+=aply_ident(
                text=self._cpu.output,
                ident=self._cpu.acumulated_ident
        )
    
    
    def compile(self,file:str)->str:
        return self._iNclude([file])
        

        


   


    def _dIscard(self,callback_args:list):
        if not self._cpu.operating:
            return None
        
        self._cpu.operating = False 
    

    def _eNd(self,callback_args:list):
        self._cpu.operating =True

    


    def _iNclude(self,callback_args:list)->str:
        if not self._cpu.operating:
            return None
        
        try:
            file = callback_args[0]
        except IndexError:
            raise IndexError('file not passed in args ')

        
        with open(file,'r') as arq:
            content = arq.read()
        
        self._syscall(content)

        
    
    def _rEf(self,callback_args:list)->str or None:
        if not self._cpu.operating:
            return None
        
        try:
            arg_to_print = callback_args[0]
        except IndexError:
            raise IndexError('reference not provided')
        
        try:
            value = self.args[arg_to_print]
        except KeyError:
            raise KeyError(f'args {self.args} not have {arg_to_print}')

        
        return str(value)
    



