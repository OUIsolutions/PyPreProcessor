from build_in_procedure import BuildInProcedure
from extras import aply_ident
from typing import List
from typing import Callable
from typing import Any
from json import loads
from registers import Registers
from pending_call import PendingCall
class PreProcessor:

    def __init__(self) -> None:
        self.args = {}
    
        self.include_name = '#include('
        self.discard_name ='#discard('
        self.end_name = '#end('
        self.ref_name = '#ref('
        self.break_char = ')'
        self._registers = Registers()
        self._pending_calls:List[PendingCall] = []
      
    
    
    def _get_procedures(self)->List[BuildInProcedure]:
        return [
            BuildInProcedure(self._iNclude,self.include_name),
            BuildInProcedure(self._rEf,self.ref_name),
            BuildInProcedure(self._dIscard,self.discard_name,simple_scope_open=True),
            BuildInProcedure(self._eNd,self.end_name,end_scope=True)
        ]
    

    def _get_possible_action(self,possible_procedure:str)->BuildInProcedure or None:
        procedures = self._get_procedures()
        for proc in procedures:
            proc:BuildInProcedure
            if possible_procedure == str(proc):
                return proc



    def _syscall(self):
            
        if self._registers.point >= self._registers.code_size:
            self._registers.compilation_result+=aply_ident(
                    text=self._registers.compilation_result,
                    ident=0
            )
            return False
    
        self._registers.add_last_char_to_stage()

    
        possible_procedure = self._get_possible_action(possible_procedure=self._registers.stage)
        if possible_procedure:
            self._pending_calls.append(
                PendingCall(possible_procedure)
            )
            
            self._registers.resset_stage()
            self._registers.point+=len(possible_procedure)
            return self._registers.next()
        
        



        return self._registers.next()
        



    def _exec_code(self,content:str):
        
        self._registers.code+=content
        self._registers.code_size+=len(content)
        while self._syscall():pass 


        

    def compile(self,file:str)->str:
        with open(file,'r') as arq:
            self._exec_code(arq.read())
        return self._registers.compilation_result
