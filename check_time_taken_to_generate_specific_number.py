from random import randint
def genrandom():
    last=""
    j=0
    while j < 8:
            r= randint(0,9)
            last+=str(r)
            j+=1
    print(last)
    
    if last == "56653435":
        print("got it")
    else:
        genrandom()
    
genrandom()       

#Disclaimer generates stack overflow error when recursive depth is reached   