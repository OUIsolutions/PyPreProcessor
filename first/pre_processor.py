from build_in_procedure import BuildInProcedure
from extras import aply_ident
from typing import List
from typing import Callable
from typing import Any
from json import loads
from registers import Registers

class PreProcessor:

    def __init__(self) -> None:
        self.args = {}
    
        self.include_name = '#include('
        self.discard_name ='#discard('
        self.end_name = '#end('
        self.ref_name = '#ref('
        self.break_char = ')'
        self._registers = Registers()

    
    
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
    
        current_char = self._registers.code[self._registers.point]
        self._registers.stage+=current_char

        try:
            raw_int = int(self._registers.stage)
            self._registers.args.append(raw_int)
            self._registers.stage = ''
        except TypeError:
            pass

        

        

        #if current_char == '\n':
        #    self._registers.acumulated_ident = started_identation
        #else:
        #    self._registers.acumulated_ident+=1
        

        self._registers.point+=1
        return True
        



    def _exec_code(self,content:str):
        
        self._registers.code+=content
        self._registers.code_size+=len(content)
        while self._syscall():pass 


        




    def compile(self,file:str)->str:
        with open(file,'r') as arq:
            self._exec_code(arq.read())
        return self._registers.compilation_result

        


   


    def _dIscard(self,callback_args:list):
        if not self._registers.operating:
            return None
        
        self._registers.operating = False 
    

    def _eNd(self,callback_args:list):
        self._registers.operating =True

    


    def _iNclude(self,callback_args:list)->str:
        if not self._registers.operating:
            return None
        
        try:
            file = callback_args[0]
        except IndexError:
            raise IndexError('file not passed in args ')

        
        with open(file,'r') as arq:
            content = arq.read()
        
        self._exec_code(content)

        
    
    def _rEf(self,callback_args:list)->str or None:
        if not self._registers.operating:
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
    



