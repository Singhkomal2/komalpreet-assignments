input_number=int(input("enter a number: "))
x=0
y=1
if (input_number%1==0 and input_number>0):
 while (input_number//y>0):
  y=y*10
  x=x+1
  print(x)
else:print("input is not valid")
       
                 
