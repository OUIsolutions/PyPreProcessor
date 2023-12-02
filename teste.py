

from src.virtual_machine import VirtualMachine



v = VirtualMachine()


v.exec([

    ["set","r",10]

    ["set","x","r"]


])

print(v.stack)