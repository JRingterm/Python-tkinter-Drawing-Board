from tkinter import *
# 그냥 import 대신 from을 사용하여 넣는다면 모듈명 tkinter 생략 가능



##### 지우개 함수 정의
def erase():
    global line_color
    global line_width
    line_color = "White"
    line_width = 15



##### 라인 너비 함수 정의
line_width = 2

def pluswidth():
    global line_width
    line_width = line_width+1
    
def minuswidth():
    global line_width
    line_width = line_width-1
    if line_width <0:
        line_width = 1


##### 색깔변경 함수 정의
line_color = "Black" #기본적인 선 색 Black

def changecolorred():
    global line_color
    line_color = "Red" #선 색 Red로
    global line_width 
    line_width = 1 #선 굵기 1

def changecolorblue():
    global line_color
    line_color = "Blue" #선 색 Blue로
    global line_width
    line_width = 1 

def changecoloryellow():
    global line_color
    line_color = "Yellow" #선 색 Yellow로
    global line_width
    line_width = 1

def changecolorgreen():
    global line_color
    line_color = "Green" #선 색 Green으로
    global line_width
    line_width = 1

def changecolorblack(): #선 색 Black으로
    global line_color
    line_color = "Black"
    global line_width
    line_width = 1

##### 캔버스 설정 변수 
canvas_height = 600 #캔버스 높이 600
canvas_width = 600 #캔버스 너비 600
canvas_colour = "white" #캔버스 색 white
canvas_cursor = "pencil"#캔버스 커서는 pencil로 설정


##### 캔버스 기초 설정
canvas = Tk() #윈도우창 만들기
canvas.title("window") #이름 지정, 무슨 이유에서인지 이 아래부터는 작동이 안됨



##### 프레임-색깔
frame=Frame(canvas) #프레임= 다른 위젯을 그룹화, 레이아웃 구성, 위젯에 패딩 제공
frame.pack(side=TOP)
##### 프레임-완료
frame1=Frame(canvas)
frame1.pack(side=BOTTOM)


##### 옵션용 버튼 설정 (밑에 있을수록 왼쪽에 위치함)


Bp =Button(frame, text="+", fg="Black", command = pluswidth)
Bp.pack(side=RIGHT)#선 굵기를 바꾸는 +버튼

Bm = Button(frame, text="-", fg="Black", command = minuswidth)
Bm.pack(side=RIGHT)#선 굵기를 바꾸는 -버튼

Be = Button(frame, text="Erase", fg="Black", command = erase)
Be.pack(side=RIGHT)#선을 지우는 Erase버튼


Bblack=Button(frame, text="Black", fg="Black", command = changecolorblack)
Bblack.pack(side=RIGHT)#색을 검은색으로 바꾸는 Black버튼


Bg=Button(frame, text="Green", fg="Green", command = changecolorgreen)
Bg.pack(side=RIGHT)#색을 초록색으로 바꾸는 Green버튼


By=Button(frame, text="Yellow", fg= "Yellow", command = changecoloryellow)
By.pack(side=RIGHT)#색을 노란색으로 바꾸는 Yellow버튼


Bb=Button(frame, text="Blue", fg="Blue", command = changecolorblue)
Bb.pack(side=RIGHT)#색을 파란색으로 바꾸는 Blue버튼

Br=Button(frame,text= "Red", fg="Red", command = changecolorred)
Br.pack(side=RIGHT)#색을 빨간색으로 바꾸는 Red버튼


B_end=Button(frame1,text = "완료")
B_end.pack(side= LEFT)#완료 버튼





#tkinter에서 캔버스 설정 만들기
paint = Canvas(canvas, bg=canvas_colour, height= canvas_height, width=canvas_width, cursor=canvas_cursor, )



##### 마우스 인식 설정
def draw(event): #캔버스에 선을 그음
    global x0, y0 #global을 써줌으로써 전역변수로 바꿔줌
    paint.create_line(x0, y0, event.x, event.y, fill=line_color, width =line_width) #선분
    x0, y0 = event.x, event.y

def down(event): #재클릭시 점 위치 잡기 위함
    global x0, y0
    x0, y0 = event.x, event.y
    
def up(event): #제자리를 클릭했다가 뗐을 시 점이 찍히도록
    global x0, y0
    if (x0, y0) == (event.x, event.y):
        paint.create_line(x0, y0, x0+1, y0+1, fill=line_color, width =line_width)
        
paint.bind("<B1-Motion>", draw)
paint.bind("<Button-1>", down)
paint.bind("<ButtonRelease-1>", up)

# 인터넷 인용



paint.pack() #불필요한걸 하나로 묶는다는데 없으면 그냥 아무것도 안됨
paint.mainloop() #입력을 기다리는 무한대기 루프
