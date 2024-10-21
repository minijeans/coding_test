def solution(str_list):
    if "r" in str_list and "l" in str_list and str_list.index("l") < str_list.index("r"):
        return str_list[:str_list.index("l")]
    elif "r" in str_list and "l" in str_list and str_list.index("l") > str_list.index("r"):
        return str_list[str_list.index("r")+1:]
    elif "r" not in str_list and "l" in str_list:
        return str_list[:str_list.index("l")]
    elif "l" not in str_list and "r" in str_list:
        return str_list[str_list.index("r")+1:]
    else:
        return []