def find_common_participants(str1, str2, r=','):
    list1 = str1.split(str(r))
    list2 = str2.split(str(r))
    common = set(list1).intersection(set(list2))
    return sorted(common)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
r = '|'
res = find_common_participants(participants_first_group, participants_second_group, r)
print(res)