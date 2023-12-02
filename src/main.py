

from .pre_processor import PreProcessor
from sys import argv
from sys import exit
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
    
    

if __name__ == '__main__':
    pass 