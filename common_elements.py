def find_common_elements(list1, list2):
    common_list = []
    for element in list1:
        if element in list2:
            common_list.append(element)
    return common_list
