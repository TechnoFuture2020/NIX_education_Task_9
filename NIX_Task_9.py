"""
	Task_9:
Создать функцию, которая принимает на вход два списка:
первый — список, который нужно очистить от определённых значений,
второй — список тех значений, от которых нужно очистить.
Например, list1 = [1, 2, 3, 4, 5], list2 = [1, 3, 4], функция должна вернуть [2, 5]
"""


def get_filtered_list(main_list, elem_to_del_list):
	i = 0

	while len(elem_to_del_list) > 0:
		if main_list[i] in elem_to_del_list:
			elem_to_del_list.remove(main_list[i])
			main_list.remove(main_list[i])
		else:
			i += 1

	return main_list


print(get_filtered_list([1, 2, 3, 4, 5], [1, 3, 4]))
