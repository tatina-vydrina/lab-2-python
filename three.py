str = 'ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;' \
'Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;' \
'Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;' \
'Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;' \
'21 год;Студент 2 курса'

listLine = str.split(';')

for i in range(len(listLine)):
	listLine[i] = listLine[i].replace('_', '')

print("%20s%20s%20s" % (listLine[0], listLine[1], listLine[2]))

for i in range(len(listLine)):
	if 'Петров' in listLine[i]:
		print("%20s%20s%20s" % (listLine[i], listLine[i+1], listLine[i+2]))