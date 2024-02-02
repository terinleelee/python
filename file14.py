##from tkinter import*
##win=Tk()
##canvas=Canvas(win,bg="yellow",width=100,height=100)
##canvas.pack()
##win.mainloop()


##from tkinter import*
##win=Tk()
##canvas=Canvas(win,bg="white",width=500,height=100)
##canvas.create_line(100,50,400,50,fill="green",width=5)
##canvas.pack(fill="both",expand=True)
##win.mainloop()
    
##from tkinter import*
##win=Tk()
##canvas=Canvas(win,bg="white",width=1000,height=1000)
##canvas.create_line(500,100,500,400,fill="red",width=5)
##canvas.pack(fill="both",expand=True)
##win.mainloop()

##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,bg="white",width=700,height=700)
##canvas.pack()
##
##x1,y1=0,50
##x2,y2=0,500
##
##for i in range(10):
##    x1+=50
##    x2=x1
##    canvas.create_line(x1,y1,x2,y2,fill="red",width=3)



##x1,y1=50,0
##x2,y2=500,0
##
##for j in range(10):
##    y1+=50
##    y2=y1
##    canvas.create_line(x1,y1,x2,y2,fill="blue",width=3)
##    
##win.mainloop()
from tkinter import*

pen_color="black"

def paint(event):
    global pen_color
    x1,y1=event.x,event.y
    x2,y2=x1+5,y1+5
    canvas.create_line(x1,y1,x2,y2,width=3,fill=pen_color)


def change_color(color):
    global pen_color
    pen_color=color
    
def clear_canvas():
    canvas.delete("all")
win=Tk()
canvas=Canvas(win,bg="white",width=500,height=200)
btn=Button(win,text="white",command = lambda:change_color("white"),bg="white",width=6)
btn1=Button(win,text="black",command = lambda:change_color("black"),bg="black",width=6)
btn2=Button(win,text="blue",command = lambda:change_color("blue"),bg="blue",width=6)
btn3=Button(win,text="green",command = lambda:change_color("green"),bg="green",width=6)
btn4=Button(win,text="yellow",command = lambda:change_color("yellow"),bg="yellow",width=6)
btn5=Button(win,text="red",command = lambda:change_color("red"),bg="red")
btn6=Button(win,text="+",command = change_color,bg="white",width=6)
btn7=Button(win,text="-",command = change_color,bg="white",width=6)
btn8=Button(win,text="clear",command = clear_canvas,bg="white",width=6)
canvas.grid(row=0,column=0,columnspan=9)
btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)
btn4.grid(row=1,column=3)
btn5.grid(row=1,column=4)
btn6.grid(row=1,column=5)
btn7.grid(row=1,column=6)
btn8.grid(row=1,column=7)
btn.grid(row=1,column=8)


win.bind("<B1-Motion>",paint)
win.mainloop()














