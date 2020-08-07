from esub_loader import get_total_list
from cvdsloader import get_ethalon_list


def combine_list(xml_file, ethalon_file):
    """
    combine into one dictionary results from xml file
    and benchmark list of reports
    """
    list_reports = get_total_list(xml_file)

    combined_dict = {
    'file name' : list_reports[0],
    'Reporting level, Perodicity': list_reports[1] + ' ' + list_reports[2],
    'Benchmark list of reports' : get_ethalon_list(list_reports[1], list_reports[2], ethalon_file),
    'Nil_Form list' : list_reports[3],
    'List of reports' : list_reports[4],
    'Nil_Form --> Benchmark' : '',
    'List of reports --> Benchmark' : '',
    'List of reports --> Nil_Form' : ''
                    }
    return combined_dict

def compare_1(list_1, list_2):
    """
    compare list2 to list1
    returns string:
    Equals - if equals
    + 'list of reports' for reports that present in list_2 and absent in list_1
    - 'list of reports' for reports that absent in list_2 and present in list_1
    """
    report_list_1 = set(list_1.sort())
    report_list_2 = set(list_2.sort())

    print(report_list_1)
    print(report_list_2)
    return




if __name__ == "__main__":
    # print(combine_list('data/MAS610_RL08_A_20190331.xml', 'data/0.data'))
    # print(combine_list('data/MAS610_RL02_A_20190331.xml', 'data/0.data'))
    # print(combine_list('data/MAS610_RL02_M_20190331.xml', 'data/0.data'))
    # print(combine_list('data/MAS610_RL02_Q_20190331.xml', 'data/0.data'))
    # print(combine_list('data/MAS610_RL03_H_20190331.xml', 'data/0.data'))
    # print(combine_list('data/MAS610_RL05_H_20190331.xml', 'data/0.data'))
    # print(combine_list('data/MAS610_RL08_H_20190331.xml', 'data/0.data'))
    # print(combine_list('data/MAS610_RL08_M_20190331.xml', 'data/0.data'))

    compare_1(['B3_3', 'B3_6', 'C1_3', 'E_2', 'J_1'], ['B3_3', 'B3_6', 'C1_3', 'E_2', 'J_1'])
