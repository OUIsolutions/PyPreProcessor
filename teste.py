

from src.virtual_machine import VirtualMachine



v = VirtualMachine()


v.exec([

    ["declare","r",10]
    
    ["declare","x",30]


])

print(v.stack)