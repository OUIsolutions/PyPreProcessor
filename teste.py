

from src.virtual_machine import VirtualMachine



v = VirtualMachine()


v.exec([

    ["set","r",["raw",20]],
    ["set","x",["ref","r"]],



])

print(v.stack)