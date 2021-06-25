f = open('score.txt')
a = 0
b = 0
c = 0
while True:
    fin = f.readline()
    for i in range(5):
     a = int(fin)
     b = (int(fin) - a)
     print(b,end='')

     break
    f.close()
