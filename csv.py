# csv 모듈
import csv
import matplotlib.pyplot as plt
f=open('기상청.csv')
print(csv.reader(f))
data=csv.reader(f)
header=next(data)
print(header)
#print(list(data))
# 1. 최고 기온만 새로운 리스드만 저장
array =[]
for row in data:
    if row[2] != '':
     array.append(float(row[1]))
     print(array)
for row in data:
    if row[2] != '':
        data=row[0].split('-')
        if data[1] == '09':
            array.append(float(row[2]))

plt.title('1month')
plt.plot(array, color='b', label='errorbar')
plt.plot(array, color='r', label='top Temperature')
plt.plot(array,'or')
#plt.axis([0,100,0,100])
plt.errorbar(array,array)
plt.grid(True)
plt.legend()
plt.show()
f.close()
