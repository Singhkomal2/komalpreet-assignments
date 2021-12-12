hh=int(input("give me the start time hour: "))
mm=int(input("give me the start time minute: "))
dd=int(input("give me the duration in  minutes: "))
k=hh*60+mm+dd
hh=k//60
mm=k-hh*60
print("the finish time is=",hh,":",mm)
       
       
