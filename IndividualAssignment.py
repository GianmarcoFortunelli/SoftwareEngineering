import random
import sys

n=0
if len(sys.argv)==2:                                         #checking error in input data
    n=sys.argv[1]
    if n.isdigit()!=True:
        exit("closing program, insert a positive number")
    elif int(n)<=0:
        exit("closing program, insert a positive number")
    else:
        n=int(n)
else:
    exit("closing program, insert only a positive number")

try:

    outFile = open("output.txt", "w") #opening output file

    outFile.write("2156257\n")

    for i in range(n):
        string=""
        m=random.randint(2,4)
        operator=random.randint(1,100) #first operator
        string=string+str(operator)
        for j in range(m): 
            operations=random.randint(1,4)   #generate operation
            if operations==1:
                string=string+"+"
            elif operations==2:
                string=string+"-"
            elif operations==3:
                string=string+"*"
            else:
                string=string+"//"
            operator=random.randint(1,100) #generate next operator
            string=string+str(operator)
        string=string+"="+str(eval(string))+"\n"   #compute result and write in the string
        outFile.write(string)

except PermissionError:
    exit("error in opening file") 
finally:
    outFile.close() #close file