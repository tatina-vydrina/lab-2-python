my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"

listLine = my_string.split(";_")

for i in range(len(listLine)):
	str = listLine[i].split(';')

	if(i == 0):
		print("%20s%20s%20s" % (str[0] + str[1] + str[2], str[3], str[4]))
	else:
		print("%20s%20s%20s" % (str[0] + ' ' + str[1] + ' ' + str[2], str[3], str[4]))
