from tkinter import *
# 그냥 import 대신 from을 사용하여 넣는다면 모듈명 tkinter 생략 가능


##### 변수설정
canvas_height = 600
canvas_width = 600
canvas_colour = "black"
canvas_cursor = "spraycan"


##### 캔버스 기초 설정
canvas = Tk()
canvas = Canvas(canvas, bg=canvas_colour, height= canvas_height, width=canvas_width, cursor=canvas_cursor, )
#배경 색, 캔버스 높이, 너비, 마우스 커서 등 
canvas.pack()
canvas.mainloop()
