"""
provide import of report lists from xml e-submission file

"""
import xml.etree.cElementTree as ET


def get_rl_id(xml_file):
    """
    :return: return rl_id value from xml filename
    """
    return xml_file[xml_file.rfind('RL'):(xml_file.rfind('RL') + 4)]


def get_p_id(xml_file):
    """
    :return: return p_id value from xml filename
    find '_'+periodicity key+'_' in name
    """
    for element_key in ('A, H, Q, M'):
        if '_' + element_key + '_' in xml_file:
            p_id = element_key
    return p_id
    # function gets xml submission file and return a dictionary of nillable reports:


def get_nil(xml_file, flag='false'):
    """
    returns a dictionary of reports as a keys and submit option as value of 'Nil_Form' element
    'xml_file' - submission xml file
    'false' (default) - return report elements with 'false' subelement
    'all' - return all report elements
    'true' - return report elements with 'true' subelements
    """
    tree = ET.ElementTree(file=xml_file)
    root = tree.getroot()
    # get Nil_Form sub elements names and get text values of subelements
    nil_dict = {}
    for element in root.findall(".//Nil_Form/"):
        for sub_element in element.findall("*"):
            #clear element.tag from usless data, leave only report name
            key_element = element.tag[element.tag.find('_', element.tag.find('_')+1,-1)+1:]
            #create dictionary with all elements
            nil_dict.update({key_element: sub_element.text})
    # return dictionary with selected 'flag'
    if flag == 'all':
        return nil_dict
    elif flag == 'false':
        false_nil_dict = {key:value for (key,value) in nil_dict.items() if value != 'true'}
        return false_nil_dict
    elif flag == 'true':
        true_nil_dict = {key:value for (key,value) in nil_dict.items() if value == 'true'}
        return true_nil_dict


def get_report_list(xml_file):
    """
    returns a list of report elements from xml submission file
    'xml_file' - submission xml file
    """
    tree = ET.ElementTree(file=xml_file)
    root = tree.getroot()
    # all children elements with attribute type="group"
    return [i.tag for i in root.findall('.//A1_x0020_Repeat_x0020_Group/*[@type="group"]') if i.tag != 'Nil_Form']


def create_report_list(xml_file):
    """
    returns a dictionary of
    'xml_file' - submission xml file
    {'file name' : 'MAS610_RL08_H_20190331.xml',
    'RL_ID':'RL08',
    'P_ID' :'H',
    'Nil_Form': (),
    'Report List': ()
    }

    """

    final_dict = {
                    'File name': xml_file,
                    'RL_ID': get_rl_id(xml_file),
                    'P_ID': get_p_id(xml_file),
                    'Nil_Form': get_nil(xml_file),
                    'Report List': get_report_list(xml_file)
                    }
    return final_dict


if __name__ == '__main__':
    # print(get_rl_id('d:\\PROG\\MAS SUB_TESTER\\test_data\\MAS1003 RL11_Q_20190331.xml'))
    # print(get_p_id('d:\\PROG\\MAS SUB_TESTER\\test_data\\MAS1003 RL11_Q_20190331.xml'))
    print(create_report_list('data/MAS610_RL08_A_20190331.xml'))
    print(create_report_list('data/MAS610_RL08_A_20190331.xml'))
    print(create_report_list('data/MAS610_RL08_A_20190331.xml'))
    print(create_report_list.__doc__)
