from tkinter import*

class Ball:
    def _init_(self,court,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

        self.x_dist=10
        self.y_dist=10

        self.width=x2-x1
        self.height=y2-y1

        self.court=court

        self.canvas=court.canvas

        self.ball=self.canvas.create_oval(x1,y1,x2,y2,fill="yellow")
def move_ball(self):
    
    self.x1+=self.x_dist
    self.y1+=self.y_dist
    
    if self.y1<=5:
        self.y1=5
        self.y_dist*=-1

    if self.y1>=(self.court.height-(self.height-5)):
        self.y1=self.court.height-(self.height-5)
        self.y_dist*=-1


    if self.self.x1<=5:
        self.x_dist*=-1
##        self.stop_ball()

    if self.x1+self.width>=self.court.width-5:
        self.x_dist*=-1
        #self.stop_ball()


    self.x1=self.x1
    self.x2=self.x1+self.width
    self.y1=self.y1
    self.y2=self.y2+self.height

    self.canvas.coords(self.ball,self.x1,self.y1,self.x2,self.y2)

    self.ball.pack()
