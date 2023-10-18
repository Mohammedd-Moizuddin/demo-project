def add (x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y
def sqr(x,y):
  return(x**y)
a=int(input("enter a:"))
b=int(input("enter b:"))
print("1,+ 2,- 3,* 4,/ 5,**")
op=int(input("enter an option"))
if op==1:
 r=add(a,b)
 print(r)
if op==2:
 r=sub(a,b)
 print(r)
if op==3:
 r=mult(a,b)
 print(r)
if op==4:
 r=div(a,b)
 print(r)
if op==5:
 r=sqr(a,b)
 print(r) 
else:
 print("error")
