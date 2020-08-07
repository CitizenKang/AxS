"""
provide import of list of reports for certain Report Level and Periodicity combination

"""

def load_f(input_file):
    """
    input_file - path to '0.data' file
    reads file and return list of elements like [RL_ID-P_ID, report_number]
    """
    with open(input_file) as file:
        file_content = file.readlines()
        list_reports = []
        for element in file_content:
            element = (element.replace('\t', ' ').replace('\n', ' '))
            list_reports.append(element.split()[1:4])

    # convert list to ['Rl_ID-O_ID', 'report']
    result_list = [[str(i[0]) + '-' + str(i[1]), i[2]] for i in list_reports]
    return result_list


def report_dict_builder(lis_of_reports):
    """
    :param lis_of_reports: list of reports with lists as elements like [RL_ID-P_ID, report_number]
    :return: dictionary with key - RL_ID-P_ID and values - list of aggregated reports numbers
    """
    d_reports = {}
    for element in lis_of_reports:
        if element[0] not in d_reports.keys():
            d_values = [element[1]] #создаем список из велью
            d_reports.update({element[0]: d_values})
        else:
            # old key, old values
            d_key = element[0]
            d_values = d_reports.get(d_key)  # вытягиваем значения словаря по ключу = эелементу[0] --> str
            if isinstance(d_values, str):
                d_reports.update({d_key: [d_values, element[1]]})
            else:
                d_values.append(element[1])
                d_reports.update({d_key: d_values})
    return d_reports

def get_ethalon_list(rl_id, p_id, input_file):
    """
    :param rl_id:
    :param p_id:
    :param input_file:
    :return: list of reports from file for certain RL_ID / P_ID
    """
    dict_key = rl_id + '-' + p_id
    ethalon_list = report_dict_builder(load_f(input_file))
    return ethalon_list.get(dict_key)
