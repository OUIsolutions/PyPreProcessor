


from typing import List
from typing import Any
from json import loads
from json import JSONDecodeError
from sys import argv
from sys import exit
import traceback


#comp: if False: #>>  #end
from pre_processor import PreProcessor
#<< 




#comp#: self.include("src/extras.py") #end 
#comp#: self.include("src/line.py") #end 
#comp#: self.include("src/code_block.py") #end 
#comp#: self.include("src/text_block.py") #end 
#comp#: self.include("src/instruction_list.py") #end 
#comp#: self.include("src/pre_processor.py") #end 





def main():
    try:
        target = argv[1]
    except IndexError:
        print('target of compilation not provided')
        exit(1)
    try:
        output = argv[2]
    except IndexError:
        print('output not provided ')
        exit(1)
    
    args = None
    try:
        args = argv[3]
    except IndexError:
        pass 

    preprocessor = PreProcessor()
    if args:
        try:
            converted_args = loads(args)
        except JSONDecodeError as e:
            print(e)
            exit(1)
        for key in args:
            value = args[key]
            preprocessor.__setattr__(value)
    try:
        result = preprocessor.run(target)
    except Exception as e:
        print(traceback.format_exc())
        exit(1)
    
        
    
    with open(output,'w') as arq:
        arq.write(result)


    


if __name__ == '__main__':
    main()