class car:
    count=0
    speed=0

    def speedchange(self,v):
        car.count +=1
        self.speed=v

bmw=car()
benz=car()

bmw.speedchange(100)
print("bmw speed:", bmw.speed)
print("number of speedchange:",car.count)

benz.speedchange(120)
print("benz speed:",benz.speed)
print("number of speedchange:", car.count)


class car:
    def __init__(self,model,color):
        self.model=model
        self.color=color

    def info(self):
        print("model:",self.model,",color:",self.color)

bmw=car("bmw","white")
bmw.info()

benz=car("benz","black")
benz.info()

class character:
    def __init__(self,name,weapon):
        self.name=name
        self.weapon=weapon

    def intro(self):
        print("name:",self.name)
        print("weapon:",self.weapon)

lugo= character("lugo","gun")
lugo.intro()


class action(character):
    step=0

    def move_forward(self,n):
        self.step +=n
        print("current location is %d." %self.step)
    def move_backward(self,n):
        self.step -=n
        print("current location is %d." %self.step)

    def turn_right(self):
        print("turn right")
    

    def turn_left(self):
        print("turn left")

lugo=action("Lugo","gun")
lugo.move_forward(10)
lugo.move_backward(3)
lugo.turn_right()
lugo.turn_left()


class tv:
    def __init__(self,channel,volume):
        self.channel=channel
        self.volume=volume
        self.power=True

    def info(self):
        print("power:",self.power)
        print("channel:",self.channel)
        print("volume:",self.volume)
    def set_channel(self,ch):
        if self.power:
            self.channel=ch
        else:
            print("turn off")

    def on_off(self):
        if self.power:
            self.power=False
            print("turn off")
        else:
            self.power=True
            print("turn on")

   
    def set_volume(self,volume):
        if self.volume:
            self.volume=volume
        else:
            print("turn off")



tv=tv("1","16")
tv.info()
tv.set_channel(8)
tv.on_off()
tv.on_off()
        
        























        
