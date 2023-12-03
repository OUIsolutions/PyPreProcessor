from first.pre_processor import PreProcessor

def main():
    p = PreProcessor()
    r =p.compile("target.py")
    print(r)
main()