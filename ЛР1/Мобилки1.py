#массив, в котором будет хранится парсинг из файла
data = []
type(data)
#открытие и считывание файла
file = open('data.txt', 'r')
[data.append(line.rstrip().split(',')) for line in file]
file.close()

#длительность звонка
call_duration = float(data[2][3]) 
#стоимость 1-ой СМС
k_sms = 1
#коэффициент стоимости исходящего вызова
k_out =  2                        
#коэффициент стоимости входящего вызова
if call_duration < 50:
	k_in = 0
else:
	k_in = 1
#расчет стоимости отправленных СМС
sms = int(data[2][4]) * k_sms
#расчет стоимости входящего звонка
in_call = call_duration * k_in
#расчет стоимости исходящего звонка
out_call = call_duration * k_out
#сумма по тарифу
summa = sms + in_call + out_call
#вывод суммы
print('Total:', summa, 'rubles')