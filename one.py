str = input("Введите строку: ")

for n in [',', '.','!','?']:
	str = str.replace(n, '')

listWords = str.split(" ")

newStr = ""

for word in listWords:
	if (len(word) >= 5):
		newStr += word + " "

print(newStr)