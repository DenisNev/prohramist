
import re
chisla = []
slova = []
Input = "Pyth14on its a 124best lan24guage24".split()
for elem in Input:
	chisla.extend(re.findall('(\d+)', elem))
for elem in Input:
	slova.append("".join(re.findall('(\D+)', elem)))
for i in range(len(chisla)):
	chisla[i] = int(chisla[i])  
for i in range(len(chisla)):
	if chisla[i] != max(chisla):
		print(pow(chisla[i], i))
print(chisla)
for i in range(len(slova)):
	slova[i] = slova[i].title()[0:-1]+slova[i][-1].upper()
print(" ".join(slova))
