from esub_loader import get_total_list
from cvdsloader import get_ethalon_list


def compareit(list_1, list_2):
    """
    Compare list2 to list1
    Returns a string:
    Equals - if equals
    + 'list of reports' for reports that present in list_2 and absent in list_1
    - 'list of reports' for reports that absent in list_2 and present in list_1
    """
    # convert to set
    report_list_1 = set(list_1)
    report_list_2 = set(list_2)

    if report_list_1 == report_list_2:
        return 'Equals'
    else:
        # find difference
        element_more = report_list_2 - report_list_1
        element_less = report_list_1 - report_list_2

        #if difference is present form string answer
        if len(element_more) > 0:
            element_more = list(element_more)
            result_more = ('+:' + ', '.join(element_more))
        else:
            result_more = ''
        if len(element_less) > 0:
            element_less = list(element_less)
            result_less = ('-:'+', '.join(element_less))
        else:
            result_less = ''
    return (result_more + ' ' + result_less).lstrip()

def combine_list(xml_file, ethalon_file):
    """
    combine into one dictionary results from xml file
    and benchmark list of reports
    """
    list_reports = get_total_list(xml_file)
    benchmark_list = get_ethalon_list(list_reports[1], list_reports[2], ethalon_file)

    combined_dict = {
    'file name' : list_reports[0],
    'Reporting level, Perodicity': list_reports[1] + ' ' + list_reports[2],
    'Benchmark list of reports' : benchmark_list,
    'Nil_Form list' : list_reports[3],
    'List of reports' : list_reports[4],
    'Nil_Form --> Benchmark' : compareit(benchmark_list, list_reports[3]),
    'List of reports --> Benchmark' : compareit(benchmark_list, list_reports[4]),
    'List of reports --> Nil_Form' : compareit(list_reports[3], list_reports[4])
    }
    return combined_dict

if __name__ == "__main__":
    print(combine_list('data/MAS610_RL08_A_20190331.xml', 'data/0.data').get('List of reports --> Benchmark'))
    print(combine_list('data/MAS610_RL02_A_20190331.xml', 'data/0.data').get('List of reports --> Benchmark'))
    print(combine_list('data/MAS610_RL02_M_20190331.xml', 'data/0.data').get('List of reports --> Benchmark'))
    print(combine_list('data/MAS610_RL02_Q_20190331.xml', 'data/0.data').get('List of reports --> Benchmark'))
    print(combine_list('data/MAS610_RL03_H_20190331.xml', 'data/0.data').get('List of reports --> Benchmark'))
    print(combine_list('data/MAS610_RL05_H_20190331.xml', 'data/0.data').get('List of reports --> Benchmark'))
    print(combine_list('data/MAS610_RL08_H_20190331.xml', 'data/0.data').get('List of reports --> Benchmark'))
    print(combine_list('data/MAS610_RL08_M_20190331.xml', 'data/0.data').get('List of reports --> Benchmark'))
