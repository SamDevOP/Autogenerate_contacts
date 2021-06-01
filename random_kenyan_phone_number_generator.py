from random import randint
#from time import clock

def genrandom():
    last=""
    j=0
    while j < 8:
            r= randint(0,9)
            last+=str(r)
            j+=1
    return last

#validate the input 
#handle the input error
start=clock()
try:
    contact=int(input("Enter the number of contacts you want: "))
    
    for i in range(0,contact):
        k=genrandom()
        #print("07" + str(k))
        print("+254" + str(k))
   
        

    #print(type(contact))
except ValueError:
    print("You have not entered an integer")

stop=clock()

print("Program took: ",stop-start )

