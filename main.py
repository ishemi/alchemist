import sys
import os

path = os.getcwd()
sys.path.append (os.path.join(path,"tools"))

import tools

def main():
    #Main function
    tools.decompress_file("alchemist.zip", ".")



if __name__ == '__main__':
    main()
