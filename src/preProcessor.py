


class PreProcessor:

    def __init__(self) -> None:
        self.include_name = 'include'
        self.ref_name = 'ref'
        self.embed_name ='embed'




    def amalgamate(file:str,args:dict,already_included:list=[]):
        with open(file,'r') as arq:
            content = arq.read()

        

        



