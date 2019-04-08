print('Вводите элементы через enter. Для окончания ввода нажмите enter')

a = int(input('> '))
myList = []

while True:
	try:
		myList.append(a)
		a = int(input('> '))

	except:
		break

print('В списке {} элементов'.format(len(myList)))

myList.pop(0)
myList.pop(0)

for i in range(2):
	n = input("Введите число: > ")
	myList.append(int(n))

print(myList)