#Solve the Tower of Hanoi problem using recursion

def tower(n,source,auxilliary,destination):
    if n == 1:
        print("Move disk1 from",source,"to",destination)

    else:
        tower(n-1,source,destination,auxilliary) 
        print("Move disk",n,"from",source,"to",destination)
        tower(n - 1,auxilliary,source,destination) 

n = int(input("Enter number of disks:")) 
tower(n,"A","B","C")       
