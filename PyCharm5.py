name = input('name')
hour = int(input('hour'))
pay = int(input('pay'))

total = hour * pay

#출력방법
#1, 콤마연산자사용
print(name,'님의 총 지금액은',total,'입니다')

#2. 형식문자(서식문자) 사용 : 정수(%d), 실수(%f), 문자열(%s)
print('알바생의 이름은? : %s 입니다.' % name)
print('총합금액은 ? : %d 입니다.' % total)

#3. 문자열 .format()함수
print('알바생의 이름은 {}입니다' . format(name)) 
print('%s님 의 총금액은 %d원 입니다'  % (name,hour * pay))


#4. f-string사용
print(f'알바생의 이름은 {name} 입니다.' )

print(f'가격은 이거다  {total} 입니다.' )


'''
print('%s님 의 총금액은 %d원 입니다', % (name,hour * pay))
'''
