def nested_list_sum(lst):
    if lst == []:
        return 0
    elif type(lst[0]) == type([]):
        return nested_list_sum(lst[0]) + nested_list_sum(lst[1:])
    else:
        return lst[0] + nested_list_sum(lst[1:])

#Test
'''
a = nested_list_sum([3,[1]])
print a
'''