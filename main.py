from first.pre_processor import PreProcessor

def main():
    p = PreProcessor()
    r =p.run("target.py")
    print(r)
main()