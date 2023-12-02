



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


from action import Action
from action_result import ActionResult
from extras import aply_ident
from typing import List
from typing import Callable
from typing import Any
from json import loads


class PreProcessor:

    def __init__(self) -> None:
        self.args = {}
        self.include_name = "include("
        self.ref_name = "ref("
        self.break_char = ')'
        self.acumulated_ident = 0
    
    
    def _get_actions(self)->List[Action]:
        return [
            Action(self._iNclude,self.include_name),
            Action(self._rEf,self.ref_name),
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
            

    



    def _iNclude(self,callback_args:list)->str:
        try:
            file = callback_args[0]
        except IndexError:
            raise IndexError('file not passed in args ')
        started_identation = self.acumulated_ident

        result = ''
        with open(file,'r') as arq:
            content = arq.read()
        content_size = len(content)
        i = 0


        while True:
            
            
            if i >= content_size:
                break
            
            current_char = content[i]
            if current_char == '\n':
                self.acumulated_ident = started_identation
            else:
                self.acumulated_ident+=1
            

            action = self._get_action_from_point(content,i)
            
            if not action:
                result+=current_char
                i+=1
                continue
            

            action_result = self._exec_action(action,content,i)
            result+=str(action_result)
            i=action_result.point

        self.acumulated_ident = started_identation 

        return aply_ident(text=result,ident=self.acumulated_ident)
        
        
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
        print(args_string)
        
        formated = loads(args_string)
        result = action.call(callback_args=formated)
        return ActionResult(text=result,point=i)




    def compile(self,file:str)->str:
        return self._iNclude([file])
        

        






def main():
    try:
        target = argv[1]
    except IndexError:
        print('target of compilation not provided')
        exit(1)
    try:
        output = argv[2]
    except IndexError:
        print('output not provided ')
        exit(1)
    
    args = None
    try:
        args = argv[3]
    except IndexError:
        pass 

    preprocessor = PreProcessor()
    if args:
        try:
            converted_args = loads(args)
        except JSONDecodeError as e:
            print(e)
            exit(1)
        preprocessor.args= converted_args
    try:
        result = preprocessor.compile(target)
    except Exception as e:
        print(e)
        exit(1)
    
    with open(output,'w') as arq:
        arq.write(result)


    


if __name__ == '__main__':
    main()