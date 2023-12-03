from first.compiler import InstructionList


c = InstructionList()
c.add_text("aaaaaaaaaa")
c.add_text("aaaaaaaaaa")
c.increase_ident()
c.add_text("aaaaaaaaaa")
c.decrease_ident()
c.add_text("aaaaaaaaaa")
c.add_text("aaaaaaaaaa")

print(c)