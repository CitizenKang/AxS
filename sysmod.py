import os


def dir_check(folder_name='INPUT'):
    """
    Create directory
    """
    path = os.getcwd() + '\\' + folder_name

    try:
        os.mkdir(path)
    except FileExistsError:
        print(f'Directory {path} already exsists!')
    return path

def directory_read(path):
    """
    Checks directory and return tuple
    element[0] - path to benchmark file
    element[1] - list of path to xml files
    """
    file_list = os.listdir(path)
    if len(file_list) == 0: return print(f'Directory {path} is empty')

    # Check for benchmark file
    if '0.data' not in file_list:
        print(f"File for benchmark reports was not found in '{path}' directory!")
        benchmark_file = None
    else:
        benchmark_file = os.path.abspath('0.data')

    # Create list for submission files:
    file_list = [i for i in file_list if i.endswith(".xml")] #check only xml files
    if len(file_list) == 0:
        print(f"No xml files found in '{path}' directory!")
        list_xml_files = None
    else:
        list_xml_files = [os.path.abspath(i) for i in file_list]

    return(benchmark_file, list_xml_files)




if __name__ == '__main__':
    # dir_check('me')
    print(directory_read(dir_check()))
