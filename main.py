from first.compiler import Compiler


c = Compiler()
c.add_text("aaaaaaaaaa")
c.add_text("aaaaaaaaaa")
c.increase_ident()
c.add_text("aaaaaaaaaa")
c.add_text_block()
c.decrease_ident()

c.add_text("aaaaaaaaaa")
c.add_text("aaaaaaaaaa")

print(c)