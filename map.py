num = [1,5,2,8,4,5,1,1]

for i in range(len(num)):
    num[i] = int(num[i])
    print(num)

num = ['10','30','40']
result=list(map(int,num))
print(result)
