from tkinter import * #GUi모듈
from tkinter import ttk

a = Tk() #Tk 클래스 객체 생성
a.title("캐치마인드") #제목 설정
a.geometry("700x500") #창 크기 설정

a1 = Button(a, text = "완료") #버튼 설정
a1.pack(side="bottom",pady=30) #Y축 공백

a.mainloop() #tkinter의 이벤트 루프 시작
