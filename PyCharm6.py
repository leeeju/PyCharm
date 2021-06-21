sid = str(input('아이디'))
spw = input('비밀번호')


if sid == 'admin':
    if spw == '1234':
        print('success')
    else:
        print('pw error')
else:
    print('sign up!')
