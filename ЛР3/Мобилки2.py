import matplotlib.pyplot as plt
#массив, в котором будет хранится парсинг из файла
data = []
byte = 0
#открытие файла
file = open('data1.txt', 'r')
#запись в массив
for line in file:
	data.append([str(i) for i in line.split()])
#число строк
n = len(data)
#считывание строки от 1 до n
for i in range(1, n):
	#поиск строки, в которой содержится строка "192.168.250.41:"
	if "192.168.250.41:" in data[i][5]:
		#общий объем трафика
		byte = byte + int(data[i][11])
#перевод из байт в Мбайт
mbyte = byte / 1000000
#множитель тарифного плана за 1 Мбайт
k = 1
#подсчет к оплате
internet = mbyte * k
#вывод
print("Total:", round(internet, 2), "rubles")
#закрытие файла
file.close()

