from tkinter import *
# 그냥 import 대신 from을 사용하여 넣는다면 모듈명 tkinter 생략 가능




##### 변수설정
canvas_height = 600
canvas_width = 600
canvas_colour = "white"
canvas_cursor = "spraycan"


##### 캔버스 기초 설정
canvas = Tk() #윈도우창 만들기
canvas.title("window") #이름 지정, 무슨 이유에서인지 이 아래부터는 작동이 안됨


##### 옵션용 버튼 설정
B=Button(canvas,text="Red", fg="Red",) #Red버튼을 누르면 빨간색이 되도록
B.pack()


#tkinter에서 캔버스 설정 만들기
canvas = Canvas(canvas, bg=canvas_colour, height= canvas_height, width=canvas_width, cursor=canvas_cursor, )


#fill="red" 이거 create line에 추가하면 선색 바뀜



##### 유저 컨트롤 설정
def draw(event):   #캔버스에 선을 그음
    global x0, y0 #global을 써줌으로써 전역변수로 바꿔줌
    canvas.create_line(x0, y0, event.x, event.y) #선분
    x0, y0 = event.x, event.y

def down(event): #재클릭시 점위치 잡기위함
    global x0, y0
    x0, y0 = event.x, event.y
    
def up(event): #제자리를 클릭했다가 뗐을 시 점이 찍히도록
    global x0, y0
    if (x0, y0) == (event.x, event.y):
        canvas.create_line(x0, y0, x0+1, y0+1)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<Button-1>", down)
canvas.bind("<ButtonRelease-1>", up)

# 인터넷 인용



canvas.pack() #불필요한걸 하나로 묶는다는데 없으면 그냥 아무것도 안됨
canvas.mainloop() #입력을 기다리는 무한대기 루프
