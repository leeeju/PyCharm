import csv
from tkinter import *
from tkinter.messagebox import *
#from tkinter.font import *
array = []
array2 = []
f = open('비밀번호1.csv') # 엑셀에 있는 아이디와 비밀 번호만을 받아서 맞으면 로그인 된다
data = csv.reader(f)

for row in data:
    array.append((row[0]))
    array2.append((row[1]))


def login():

    def cat():
        w2 = Toplevel(w)
        w2.title('사진 열람')  # 윈도우 생성창 이름
        img = PhotoImage(file='고양이1.png')
        img1 = PhotoImage(file='토끼.png')
        img2 = PhotoImage(file='사슴.png')
        img3 = PhotoImage(file='닭.png')
        t2 = Label(w2, text='동물사진', font=('궁서체', 20))
        t2.pack()

        sname = Label(w2, text='동물이름?', font=('궁서체', 10))
        sname.place(x=125, y=460)
        name = Entry(w2, font=t)
        name.place(x=200, y=440) # 동물 이름 입력

        name.get()
        cat2 = '고양이'
        rabbit = '토끼'
        deer = '사슴'
        chicken = '닭'

        if name == cat2:
            showinfo('정답입니다.')

        if name == chicken:
            showinfo('정답입니다.')
        if name == deer:
            showinfo('정답입니다.')
            change1()
        if name == rabbit:
            showinfo('정답입니다.')
        else:
            showinfo('틀럈습니다')

        g2 = Label(w2, image=img)
        #g3 = Label(w2, image=img2)
        g2.pack()  # 고양이
        #g3.pack()  # 토끼

        def change(): # 변환 코드
            g2.config(image=img1)
        def change1():
            g2.config(image=img2)
        def change2():
            g2.config(image=img3)
        def change3():
            g2.config(image=img)

        rbtn1 = Button(w2, text='토끼', command=change)  # 버튼 이름
        rbtn2 = Button(w2, text='사슴', command=change1)  # 버튼 이름
        rbtn3 = Button(w2, text='닭', command=change2)  # 버튼 이름
        rbtn4 = Button(w2, text='고양이', command=change3)
        #rbtn2 = Radiobutton(w2, text='이전', command=change)  # 버튼 이름

        rbtn1.place(x=160, y=350)  # 버튼 생성
        rbtn2.place(x=260, y=350)
        rbtn3.place(x=360, y=350)
        rbtn4.place(x=460, y=350)
        #rbtn2.place(x=200, y=600)

        w2.geometry('600x600')  # 2번
        w2.mainloop()  # 화면 띄우기

    a = sid.get()
    b = pw1.get()
    (len(array))
    for i in range(len(array2)): # i 를 변수로 엑셀을 전부 읽는다
     if array[i] == a and array2[i] == b:
      showinfo('본인 확인성공',' 접속합니다 \n 환영합니다 주현님')
      cat()

     else:
      showinfo('', '비밀번호 재입력')

def cancel():
    #print('cancel')
    showinfo('cancel','취소눌러짐')

w = Tk()
w.title('사진 검색 프로그램') # 윈도우 생성창 이름
t = Label(w,text='사진 검색', font=('궁서체',20))
rid = Label(w,text='아이디 입력', font=('궁서체',10))
rpw = Label(w,text='비밀번호 입력', font=('궁서체',10))
sid = Entry(w,font=t)
pw1 = Entry(w,show='*', font=t) # 비빌번호 표시 생성


if input():
 btn1 = Button(w,text='확인',command = login) # 버튼 이름
 btn2 = Button(w,text='취소',command = cancel)
 btn3 = Button(w,text='종료', command= quit) # 종료에 커맨드로 명령어 입력
# 위젯 베치 : pack(), place(), grid()

 t.pack()
 rid.place(x=30, y=45)
 rpw.place(x=30, y=65)
 sid.place(x=130, y=40)
 pw1.place(x=130, y=60)
 btn1.place(x=140, y=120) # 버튼 생성
 btn2.place(x=190, y=120)
 btn3.place(x=240, y=120)

w.geometry('400x200')  # 크기 조절
w.mainloop() # 화면 띄우기


