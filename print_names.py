import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <your string>")
        return
    
    input_string = " ".join(sys.argv[1:])
    print(input_string)

if __name__ == "__main__":
    main()

