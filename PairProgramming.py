import random
import time

choice='1'

while choice=='1':
    tic = time.perf_counter()   #start timer

    wrongList=[]

    n=10
    for i in range(n):
        string=""
        m=random.randint(2,4)   #define number of operation
        operator=random.randint(1,100) #first operator
        string+=str(operator)
        for j in range(m): 
            operations=random.randint(1,4)   #generate operation
            if operations==1:
                string+="+"
            elif operations==2:
                string+="-"
            elif operations==3:
                string+="*"
            else:
                string+="//"
            operator=random.randint(1,100) #generate next operator
            string+=str(operator)
        print("Please insert the result of the equation", string, "= ?")
        res=input()                                   #ask for user reply
        if not res.isdigit():
            wrongList.append(string + " = " + str(eval(string)))   #if it's not a number is wrong
        else:
            if int(res)!=eval(string):
                wrongList.append(string + " = " + str(eval(string)))  #if it's not correct also

        
    toc = time.perf_counter()   #stop timer 

    print("total time is ", toc-tic)
    print("total right answer is ", 10-len(wrongList)) #print output
    print("Your wrong answers are:")
    for answer in wrongList:
        print(answer)
    choice=input("select your choice: \t1) continue\n \t\t\t2) quit\n")
