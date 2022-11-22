n = int(input('Enter no of processes: '))
bt = [0] * (n + 1)
at = [0] * (n + 1)
abt = [0] * (n + 1)
p=    [0] * (n + 1)
for i in range(n):
    abt[i] = int(input('Enter the burst time for process {} : '.format(i + 1)))
    at[i] = int(input('Enter the arrival time for process {} : '.format(i + 1)))
    p[i] = int(input('Enter the priority for process {} : '.format(i + 1)))  
    bt[i] = [abt[i], at[i],p[i], i]

print(at) #Printing Arival Time
print(bt) #Printing the list of Burst Time, Arrival Time, ProcessID
bt.pop(-1) #Removing 0
print(abt)
print(bt)
sumbt = 0
i = 0
ll = []
for i in range(0, sum(abt)):
    l = [j for j in bt  if j[1] <= i] #Appending all processes which are less than cureent second.
    l.sort(key=lambda x: x[2], reverse=True) #Sort on basis of Burst Time.
    print(l)
    bt[bt.index(l[0])][0] -= 1 #Reducing the Burst Time of that process by 1
    for k in bt:
        if k[0] == 0: #If a process has been completed remove it.
            t = bt.pop(bt.index(k))
            ll.append([k, i + 1]) #Whichever process is donw, that is being saved here. i+1 is completion
print(ll)
ct = [0] * (n + 1)
tat = [0] * (n + 1)
wt = [0] * (n + 1)
for i in ll:
  #ll- [[[0,1, 2], 1]..]
    print(i, i[0], i[1], i[0][3])
    ct[i[0][3]] = i[1]
    #abt[i[0][3]] = i[0][2]

for i in range(len(ct)):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - abt[i]
ct.pop(-1)
wt.pop(-1)
tat.pop(-1)
abt.pop(-1)
at.pop(-1)
p.pop(-1)
print('P\tBT\tAT\tCT\tTAT\tWT')
for i in range(len(ct)):
    print("{}\t{}\t{}\t{}\t{}\n".format(p[i],abt[i], at[i], ct[i], tat[i], wt[i]))
print('Average Waiting Time = ', sum(wt)/len(wt))
print('Average Turnaround Time = ', sum(tat)/len(tat))
