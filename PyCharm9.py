mport random

print('구구단 게임')
print('구구단게임 종료 >> Y/N')

while True:
    dan = random.randint(2,9)
    num = random.randint(1,9)
    print(f'{dan} X {num} = ', end=' ')
    num2 = int(input(''))

    if num2 == dan * num:
        print('정답입니다')

    input_text = input('>종료할까요? (y/n)')
    if input_text in ['Y''N']:
        print('종료합니다')

    break
