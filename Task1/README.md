import re

#оглашение масивов

chisla = []
slova = []

#тот самый ряд который програма будет разделять

Input = "Pyth14on its a 124best lan24guage24".split()

#цикл для обработки цифр 

for elem in Input:
	chisla.extend(re.findall('(\d+)', elem))
	
#цикл для обработки слов

for elem in Input:
	slova.append("".join(re.findall('(\D+)', elem)))
for i in range(len(chisla)):
	chisla[i] = int(chisla[i])
	
#цикл для поднесения в степень  

for i in range(len(chisla)):
	if chisla[i] != max(chisla):
		print(pow(chisla[i], i))
print(chisla)

#цикл для первой и последней буквы

for i in range(len(slova)):
	slova[i] = slova[i].title()[0:-1]+slova[i][-1].upper()
print(" ".join(slova))
