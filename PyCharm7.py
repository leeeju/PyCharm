# 1, 1~10까지의 합계를 출력 하시오.  -> 사용자 = 시작/종료 = 합계
'''''
sums = int(input('숫자 입력 : '))
sums2 = int(input('종료 숫자 : '))

nums = sums + sums2
for i in range(sums,sums2):
    #sums += i
    print(f'{sums} + {i} = {sums+i}')
    print('출력 : ',nums)
'''''
hap, even, odd = 0, 0, 0
s = int(input('시작 : '))
e = int(input('종료 : '))
for i in range(s, e + 1):
    hap += i
    if i %2 == 0:
        even += i
    else:
        odd += i
        print('hap', hap)

# 2-1, 사용자로부터 성적을 입력 받아 리스트에 저장 후 저장된 데이터를
# 출력 하시오, 단 시험의 응시자는 달라진다
score = []
m = int(input('점수 : '))
for i in range(m):
    s = int(input('score:'))
    score.append(s)

print('점수 : ')
hap = 0
for i in score:
    hap += i
# for i in range(n)
#       hap += score[i]
avg = hap / len(score)
print('평균 : ', avg)
# 2-2 응시자의 평균을 하세요.
large,small=-1,101
for i in range(m):
    if score[i] > large:
        large = score[i]
    if score[i] < small:
        large = score[i]

print('최대',large)
print('최소',small)
