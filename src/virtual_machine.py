

class VirtualMachine:

    def __init__(self) -> None:
        self.stack = [{}]            
        self.stack_point = 0
        self.instruction_point = 0
        self.instructions = []
    

    def _get_value(self,value:list or str):
        if isinstance(value,list):
           return self.stack[value[0]]
        return value
    
    def _instruction_declare(self,values:list):
        self.stack[self.stack_point][values[0]] = self._get_value(values[1])




    def _syscall(self):
        try:
            current_instruction = self.instructions[self.instruction_point]
        except IndexError:
            raise IndexError(self.instruction_point)

        try:
            action =current_instruction[0]
            args = current_instruction[1::]
        except IndexError:
            raise IndexError("instruction not formated")

        action_function =  self.__getattribute__(f'_instruction_{action}')
        action_function(args)


    def exec(self,content:list):
        for r in content:
            self.instructions.append(r)
            self._syscall()  
            self.instruction_point+=1


    
    