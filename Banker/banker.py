import numpy as np
def check(i):
    for j in range(no_r):
        if(needed[i][j]>available[j]): #if greater, then return 0
            return 0
    return 1
no_p = 5 #No of Processes
no_r = 4 #No of resources
Sequence = np.zeros((no_p,),dtype=int) #Seq Empty array, for printing safe seq.
visited = np.zeros((no_p,),dtype=int) #Checks if processes Done
allocated = np.array([[4,0,0,1],[1,1,0,0],[1,2,5,4],[0,6,3,3],[0,2,1,2]]) #allocated
maximum = np.array([[6,0,1,2],[1,7,5,0],[2,3,5,6],[1,6,5,3],[1,6,5,6]]) #maximum
needed = maximum - allocated #cal needed
available = np.array([3,2,1,1]) # At the instant, available resources
count = 0 #Number of process tak
while( count < no_p ):
    temp=0
    for i in range( no_p ): #sequential search down
        if( visited[i] == 0 ): #visited =0, matlab not explored
            if(check(i)): #if check gets 0, then dont executed
                Sequence[count]=i;
                count+=1 #after process is complted
                visited[i]=1
                temp=1
                for j in range(no_r):
                    available[j] += allocated[i][j] 
    if(temp == 0): #no one satisfies cond
        break
if(count < no_p):
    print('Deadlock detected!')
else:
    print("The system is Safe")
    print("Safe Sequence: ",Sequence)
    print("Available Resource:",available) #Total available at end.
