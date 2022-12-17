from tkinter import* 
from tkinter import ttk

b = Tk()
b.title("캐치마인드")
b.geometry("200x250")

b1 = Label(b, text = "정답") #tkinter에서의 텍스트 혹은 이미지를 표시
b1.pack(pady=30) #pack= 위치 및 공간을 다루는 옵션

b2 = Entry(b) #라인 텍스트 박스 생성
b2.pack(pady=30)

b3 = Button(b, text = "제출") #단순한 버튼 생성
b3.pack(pady=30)

b.mainloop()
