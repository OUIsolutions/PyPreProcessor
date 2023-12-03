from first.instruction_list import InstructionList


c = InstructionList()
c.add_text_to_last_instruction("aaaaaaaaaa")
c.add_text_to_last_instruction("aaaaaaaaaa")
c.increase_ident()
c.add_text_to_last_instruction("aaaaaaaaaa")
c.decrease_ident()
c.add_text_to_last_instruction("aaaaaaaaaa")
c.add_text_to_last_instruction("aaaaaaaaaa")

print(c)