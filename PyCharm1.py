

grad = float(input("점수 : "))
toelc = int(input("토익 : "))


if toelc >= 700 and grad >= 4.0:
    print('면접대상자')
elif toelc >= 700 and grad >= 3.5:
    print('서류전형대상자')
elif toelc >= 700 and grad >= 3.0:
    print('필기시험대상자')

else:
    print('지원불가')
