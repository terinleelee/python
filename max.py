##def get_max(x,y):
##    if x > 0:
##        return x
##    else:
##        return y
##    
##x = int(input())
##y = int(input())
##
##n = get_max(x,y)

##def plus(x):
##    if x > 0:
##        return print("true")
##        
##    else:
##        return  print("false")
##       
##
##x = int(input(" 정수를 입력하시오 .:"))
##plus(x)

##def get_sum(n):
##    s = 0
##    for i in range(1, n+1):
##        s+=i
##    return s
##
##
##n= int(input())
##print("1부터 %d까지의 합은 %d입니다." % (n, get_sum(n)))
##def get_sum(a,b):
##    s=0
##    for i in range(a,b+1):
##        s+=i
##    return s
##
##
##a= int(input())
##b= int(input())
##print("%d부터 %d까지의 합은 %d입니다." % (a,b,get_sum(a,b)))

##def area(n,m):
##    return n*m
##
##    
##
##a = int(input())
##b= int(input())
##print(area(a,b))

##def area(a):
##    return(a*a*3.14)
##
##a=int(input())
##print(area(a))

##def number(n):
##    if n % 2==0:
##        return print("even")
##    else:
##        return print("odd")
##
##        
##n=int(input())       ## n = "5"
##number(n)

##def square(a,b):
##    return(a**b)
##
##a=int(input())
##b=int(input())
##
##
##print(square(a,b))

##def get_sum(n):
##    s=0
##    for i in range(n):
##        s += int(input())  
##    return s
##
##n=int(input("enter integer n : "))
##print("sum :",get_sum(n))

##def get_max(n):
##    s=0
##    max=0
##    for i in range(n):
##        s = int(input())
##        if s > max:
##            max=s  
##            
##        
##    return max
##
##n=int(input("enter integer n : "))
##print("max value :",get_max(n))

def rect(w,h) :
    return w*h

def tri(w,h):
    return w*h/2

def circle(r):
    return r ** 2 * 3.14

print("choose a shape :")
print("1. rectangle","2. triangle", "3. circle", sep = '\n')
n= int(input())

##if n == 1 :
##    w=int(input("width : "))
##    h=int(input("height : "))
##    area = rect(w,h)
##
##elif n == 2 :
##    w=int(input("width : "))
##    h=int(input("height : "))
##    area = tri(w,h)
##
##elif n == 3 :
##    r=int(input("radius : "))
##    area = circle(r)
##
##print(area)
     

