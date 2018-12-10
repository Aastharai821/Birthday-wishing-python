
from datetime import datetime
#from datetime import date
import time

def main():
    n=int(input("How many elderly people are there in the old age home?"))
    name_list= []
    month_list= []
    days_list= []
    for i in range(0,n):
        x=input("Give the "+str(i+1)+ "st name: ")
        name_list.append(x)
        y=datetime.strptime(input("Give his/her birthday (m/d/y): "), '%m/%d/%Y')
        month=y.month
        day=y.day
        month_list.append(month)
        days_list.append(day)

        #current time
        current_month=int((datetime.now().strftime("%m")))
        current_day=int((datetime.now().strftime("%d")))
        

    #to check the array item from month_list
    for i in range(0,n):
        if month_list[i]==current_month:
            if days_list[i]==current_day:
                print("Happy Birthday to you " +name_list[i]+ "!!!!!")
                  
 
if (__name__ == "__main__"):
    main()