import random

print('나랑 숫자 게임을 하자')
print('너의 이름은 뭐당가? ')
name = input('내이름은 :')
print('반가워 ',name)
print('내가 씨방 1부터 30 까정 들고있어 맞춰 보랑깨')
count = int(input('반복횟수는 말여? : ' ))

print('기회는 총 ' ,count ,'번이라고' )

#while True:
while count:
    player = int(input(f' 도전입력 :   {count} 번 남았다~'))
    r = random.randint(1,30)
    count -= 1
    if player == 0:
        break
    elif player == r:
        print('정답 이랑깨 ')
        break
    elif player > r:
        print('잘좀 혀봐~ 손목 날아가 붕깨')
    else:
        print('야들아~ 묻으러 가자~ ')
