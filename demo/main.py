import sys
import subprocess

def main():
    process = subprocess.Popen(["./detection", "./input.txt"], stdout=subprocess.PIPE)
    output, err = process.communicate()
    output = output.decode("utf-8")
    sys.stdout.write(output)
    
    output = int(output)
    if (output)>1:
        print(f"{output} eggs detected")
    else:
        print(f"{output} egg detected")
    
if __name__ == "__main__":
    main()
