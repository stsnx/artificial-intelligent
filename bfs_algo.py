from random import random, randrange
Target = []
Map =[]
way = "|\+!%^"

class node:
    def __init__(self,attr,visited='0',prev=[-1,-1]) :
        self.attr = attr
        self.visited=visited
        self.prev=prev
def bfs(start,finish,wp):
    execCount=0
    q = []
    q.append(start)
    Map[start[0]][start[1]].visited='1'
    Map[finish[0]][finish[1]].visited='0'
    Map[start[0]][start[1]].prev=[-1,-1]
    while len(q)>0:
        execCount+=1
        temp = q.pop(0)
        Map[temp[0]][temp[1]].visited='1'
        #if wp==2:
            #print("node"+str(temp)+" prev "+str(Map[temp[0]][temp[1]].prev)+"finish "+str(finish) +" "+ str(Map[finish[0]][finish[1]].visited))
        if temp[1]>0:
            if Map[temp[0]][temp[1]-1].visited=='0':
                Map[temp[0]][temp[1]-1].prev = [temp[0],temp[1]]
                q.append([temp[0],temp[1]-1])
        if temp[1]<9:
            if Map[temp[0]][temp[1]+1].visited=='0':
                Map[temp[0]][temp[1]+1].prev = [temp[0],temp[1]]
                q.append([temp[0],temp[1]+1])
        if temp[0]>0:
            if Map[temp[0]-1][temp[1]].visited=='0' :
                Map[temp[0]-1][temp[1]].prev = [temp[0],temp[1]]
                q.append([temp[0]-1,temp[1]])
        if temp[0]<9: 
            if Map[temp[0]+1][temp[1]].visited=='0' :
                Map[temp[0]+1][temp[1]].prev = [temp[0],temp[1]] 
                q.append([temp[0]+1,temp[1]])
        if temp == finish :
            print("found")
            PreviousPoint=Map[temp[0]][temp[1]].prev
            while PreviousPoint!=start:
                #print("prevend" + str(Map[PreviousPoint[1]][PreviousPoint[0]].prev))
                Map[PreviousPoint[0]][PreviousPoint[1]].attr = way[wp]
                PreviousPoint=Map[PreviousPoint[0]][PreviousPoint[1]].prev 
            #print("end" + str(Map[temp[1]][temp[0]].prev))
            Map[start[0]][start[1]].visited = '1'
            Map[finish[0]][finish[1]].visited = '1'
            print("execcount = "+str(execCount))
            return 1
    return 0
def resetvisited():
    for i in range(10):
        for j in range(10):
            if Map[i][j].attr=="-":
                Map[i][j].visited='0'
def set(Map):
    for i in range(10):
        for j in range(10):
            if Map[i][j].attr != "x":
                Map[i][j].attr = "-"
            Map[i][j].visited = '0'

for i in range(10):
    temp = []
    for j in range(10):
        temp.append(node("-"))
    Map.append(temp)
x= [0,7,2,9,4,1,5,1]
y= [1,9,1,5,4,5,2,0]
for i in range(len(x)):
    position = [y[i],x[i]]
    Map[y[i]][x[i]].attr = 'x'
    Target.append(position)
print(Target)
wp = 0
success=0
for j in range(len(x)//2):
    for i in range(len(x)//2):
        start = Target.pop(0)
        Target.append(start)
        finish = Target.pop(0) 
        Target.append(finish)
        print("bfs"+ str(start))
        success+=bfs(start,finish,wp)
        wp+=1
        resetvisited()
    print(success)
    if success<len(x)//2 and j!=len(x)//2-1:
        temp = Target.pop(0)
        Target.append(temp)
        temp = Target.pop(0)
        Target.append(temp)
        set(Map)
        wp = 0
        success=0
    else :
        break
for i in range(10):
    for j in range(10):
        print(Map[i][j].attr,end=' ')
    print()
for i in range(10):
    for j in range(10):
        print(Map[i][j].visited,end=' ')
    print()

