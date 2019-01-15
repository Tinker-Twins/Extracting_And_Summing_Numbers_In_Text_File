import re
handle = open('File.txt')
total = 0
lst=list()

for line in handle:
	line = line.rstrip()
	l = re.findall('[0-9]+',line)
	for num in l:
		lst.append(num)
for val in lst:
	i = int(val)
	total = total + i
print(total)