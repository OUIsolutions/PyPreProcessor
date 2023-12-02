

class VirtualMachine:

    def __init__(self) -> None:
        self.stack = []
        self.code_line = 0
        self.lines = []
    
    

    def line_interpreter(self,line:str):
        pass 

    def exec(self,content:str):
        pass 
    

    def exec_file(self,file:str):
        with open(file,'r') as arq:
            self.exec(file)

    