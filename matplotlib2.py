import matplotlib.pyplot as plt
import csv
f=open('월드컵.csv')
data=csv.reader(f)
header=next(data)
print(header)
#print(list(data))

array = []
for row in data:
    if row[0] != '':
        array.append(row[1])
        array = list(map(float, array))
print(array,end='')

plt.title('aa')
plt.plot(array, color='b', label='aa')
plt.plot(array, color='r', label='aa')
plt.plot(array,'or')
plt.show()
