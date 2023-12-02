


include("boostraping/imports.py")
include("boostraping/action_result.py")
include("boostraping/action.py")
include("boostraping/extras.py")
include("boostraping/pre_processor.py")



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
        preprocessor.args= converted_args
    try:
        result = preprocessor.compile(target)
    except Exception as e:
        print(e)
        exit(1)
    
    with open(output,'w') as arq:
        arq.write(result)


    


if __name__ == '__main__':
    main()