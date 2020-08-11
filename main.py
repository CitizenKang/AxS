import time
import sysmod



def main():
    print("Program started!")
    path = sysmod.dir_check()
    time.sleep(1)
    print("Copy all your xml submission files into 'INPUT' directory")
    print("Copy '0.dat' file into 'INPUT' directory")
    print(path)

    print(sysmod.directory_read(path))



    return



if __name__ == '__main__':
    main()
