#import tkinter

from tkinter import *
from tkinter.messagebox import *

def ok():
    #print('ok')
    showinfo('ok', pw.get())
    #t.config(image=photo2) # 위젯 내용 변경
def cancel():
    #print('cancel')
    showinfo('cancel', '취소눌러짐')

w = Tk() # 윈도우 생성  (k 는 소문자)
w.title('첫번쨰 gui') # 윈도우 생성창 이름
t=Label(w,text='고양이 실험실', font=('궁서체',20))
photo1 = PhotoImage(file='고양이1.png') #이미지 불러오기
#photo2 = PhotoImage(file='고양이2.png')

r=Label(w,image=photo1)
pw = Entry(w,show='*', font=t) # 비빌번호 표시 생성

btn1 = Button(w,text='확인',command=ok) # 버튼 이름
btn2 = Button(w,text='취소',command=cancel)
btn3 = Button(w,text='종료', command=quit) # 종료에 커맨드로 명령어 입력
# 위젯 베치 : pack(), place(), grid()

t.pack()
r.pack()
pw.pack()
btn1.pack() # 버튼 생성
btn2.pack()
btn3.pack()

w.geometry('600x650')  # 크기 조절


w.mainloop() # 화면 띄우기
