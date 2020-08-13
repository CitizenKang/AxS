import os
import time

import sysmod
from compare_logic import combine_list
from export_xls import xl_file, xl_cosmetics



def main():
    input_path = os.path.join(os.getcwd(), 'INPUT')

    if os.path.isdir(input_path):
        pass
    else:
        try:
            os.mkdir(input_path)
            print(f'{input_path} directory created')
        except FileExistsError:
            print(f'Directory {input_path} already exsists!')

    # Create list of files in input directory
    file_list = os.listdir(input_path)
    # Checking for total files presence in the directory
    if len(file_list) == 0: return print(f'Directory "{input_path}" is empty!')
    # Checking for 0.data file
    if '0.data' not in file_list:
        print(f"File for benchmark reports was not found in '{input_path}' directory!")
        benchmark_file = None
    else:
        benchmark_file = ('INPUT/' + '0.data')
        print(benchmark_file)
    # Checking for esub xml files in the directory:
    file_list = [f for f in file_list if f.endswith('.xml')]
    if len(file_list) == 0: xml_file_list = None
    else: xml_file_list = file_list
    if xml_file_list is None or benchmark_file is None:
        print("U can't proceed")
    else:
        print(f"Total amount of eSub to be analyzed: {len(xml_file_list)}")
    # make relative path to xml
    xml_file_list = ['INPUT/' + f for f in xml_file_list]

    list_export = []
    counter = 0
    for element in xml_file_list:
        try:
            #Create dictionary of dictionaries
            list_export.append(combine_list(element, benchmark_file))
            print(element, '- -> processed!')
            counter += 1
        except:
            print(element, '- -> Error!')

    print(f'Successfully processed {counter} files of {len(xml_file_list)}!')

    print('Exporting to excel...')
    a = xl_file(list_export)
    xl_cosmetics(a)
    print(f'Done!, check {a}')

if __name__ == '__main__':
    main()
