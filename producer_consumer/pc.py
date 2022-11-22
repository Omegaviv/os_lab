MAX=3

def Producer(l):
  if len(l) <MAX:
     print(f"Inserting {len(l)+ 1} in buffer")
     l.append(len(l)+ 1)  
  else:
    print("Buffer is Full")
  return l

def Consumer(l):
  if len(l) !=0:
    print(f"Consuming {len(l)} from buffer")
    l.pop()
  else:
    print("There is nothing in buffer")
  return l

l=[]
while (True):
  print("1- Producer")
  print("2- Consumer")
  print("3- Exit")
  print("Enter your Choice")
  x=int(input())
  if x==1:
    l=Producer(l)
  if x==2:
    l=Consumer(l)
  if x==3:
    break