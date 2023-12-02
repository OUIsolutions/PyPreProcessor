

from src.virtual_machine import VirtualMachine



v = VirtualMachine()


v.exec([

    ["set","r",["raw",20]]

    ["set","x","r",["raw",30]]


])

print(v.stack)