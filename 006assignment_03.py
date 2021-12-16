hour=int(input("provide me the start time hour: "))
minute=int(input("provide me the start time minute: "))
day=int(input("provide me the duration in minutes: "))
day=(hour*60)+minute+day
print("the finish time is: ",end="")
print(day//60,day%60,sep=":")
