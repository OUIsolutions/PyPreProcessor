

#comptime:self.include("a.txt")
#comptime:if self.args['t'] == 20:
r = 30 
class Soma:
    def __init__(self) -> None:
        #comptime:if r == 20 #do
        pass
        #end
        