year=int(input("enter the year: "))
if year<1582:
    print("not within gegorion calender")
elif year%4 != 0 :
   print("common year")
         
elif year%100 :
    print("leap year")
    
elif year%400 :
    print("common year")

else:
    print("leap year")
        
