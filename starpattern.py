
for i in range (1,6):
    for j in range(i):
       print("*",end=" ")
    print()



    
for i in range (5,0,-1):
    for j in range(i):

       print("*",end=" ")
    print()



   
for i in range (0,10):
    for j in range(i+1):

       print(j+1,end=" ")
    print()




for i in range (10,0,-1):
    for j in range(i):

       print(j+1,end=" ")
    print()

    

n=11
for i in range(n):
    for j in range(n):
        x=i-n//2
        y=j-n//2
        d1=abs(x)
        d2=abs(y)
        d3=abs(x+y)
        d4=abs(x-y)
        m=max(d1,d2,d3,d4)
        if m<=n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()