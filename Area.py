n=int(input("enter your choice: 1.base & height, 2. sides "))
if(n==1):
   b=int(input("enter base:"))
   h=int(input("enter height:"))
   if(b>=0) and (h>=0):
      a=0.5*b*h
      print("area of triangle for your choice=",a)
   else:
      print("invalid input")
elif(n==2):
   a1=int(input("enter side a:"))
   b1=int(input("enter side b:"))
   c1=int(input("enter side c:"))
   if(a1>=0) and (b1>=0) and (c1>=0):
      s=(a1+b1+c1)/2
      area=s*(s-a1)*(s-b1)*(s-c1)
      area1=area**0.5

      print("area of triangle for your choice=",area1)
   else:
      print("invlid input")
else:
   print("invalid choice")
