"""
provide import of report lists from xml e-submission file

"""
import xml.etree.cElementTree as ET
import ntpath


def get_rl_id(xml_file):
    """
    return rl_id value from xml filename
    'xml_file' - path to submission xml file
    """
    return xml_file[xml_file.rfind('RL'):(xml_file.rfind('RL') + 4)]


def get_p_id(xml_file):
    """
    return p_id value from xml filename

    'xml_file' - path to submission xml file
    """
    #find '_'+periodicity key+'_' in name
    for element_key in ('A, H, Q, M'):
        if '_' + element_key + '_' in xml_file:
            p_id = element_key
    return p_id
    # function gets xml submission file and return a dictionary of nillable reports:


def get_nil(xml_file, flag='false', return_list=True):
    """
    returns a list of reports of 'Nil_Form' element
    'xml_file' - path to submission xml file
    flag - 'false' (default) - return report elements with 'false' subelement
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
    # create and return list with selected 'flag'
    if flag == 'all':
        nil_list = [i for i in nil_dict.keys()]
        return nil_list
    elif flag == 'false':
        nil_list = [key for key in nil_dict.keys() if nil_dict[key] == 'false']
        return nil_list
    elif flag == 'true':
        nil_list = [key for key in nil_dict.keys() if nil_dict[key] == 'true']
        return nil_list


def get_report_list(xml_file):
    """
    returns a list of report elements from xml submission file
    'xml_file' - submission xml file
    """
    tree = ET.ElementTree(file=xml_file)
    root = tree.getroot()
    # all children elements with attribute type="group"
    return [i.tag for i in root.findall('.//A1_x0020_Repeat_x0020_Group/*[@type="group"]') if i.tag != 'Nil_Form']


def get_total_list(xml_file):
    """
    'xml_file' - path to submission xml file
    returns a tuple with elements:
    0 - xml file name
    1 - report level
    2 - periodicity level
    3 - report list from 'Nil_Form' element,
    4 - report list from submission xml file
    """
    # extract filename from path
    xml_file_name = ntpath.basename(xml_file)
    total_list = (xml_file_name, get_rl_id(xml_file), get_p_id(xml_file),
                get_nil(xml_file, 'false'), get_report_list(xml_file))
    return total_list

if __name__ == '__main__':

    a = get_nil('INPUT/MAS610_RL08_A_20190331.xml')
    print(a)
