from random import randint

a = []
for i in range(30):
	a.append(randint(-100, 100))
print (a)

maximum = a[0] 
for i in a:
	if i>maximum:
		maximum=i	
index = a.index(maximum)
print ("Максимальный элемент:", maximum, "Его индекс: ", index)

for i in range(len(a)):
	if i < len(a)-1:
		if a[i] < 0 and a[i+1] < 0:
			print(a[i],a[i+1])