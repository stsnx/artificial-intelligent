from random import random, randrange
Target = []
Map =[]
line_pattern = "|\+!%^"

class node: #node structure of each point in map
    def __init__(self,attribute,visited='0',previous=[-1,-1]) :
        self.attribute = attribute
        self.visited=visited
        self.prev=previous
def bfs(start,finish,way_pattern): #normal breath first search
    executeCount=0
    bfs_queue = []
    bfs_queue.append(start)
    Map[start[0]][start[1]].visited='1'
    Map[finish[0]][finish[1]].visited='0'
    Map[start[0]][start[1]].prev=[-1,-1]
    while len(bfs_queue)>0:
        executeCount+=1
        temp = bfs_queue.pop(0) #temp is first position in queue for search in bfs
        Map[temp[0]][temp[1]].visited='1'
        #if wp==2:
            #print("node"+str(temp)+" prev "+str(Map[temp[0]][temp[1]].prev)+"finish "+str(finish) +" "+ str(Map[finish[0]][finish[1]].visited))
        if temp[1]>0:
            if Map[temp[0]][temp[1]-1].visited=='0':
                Map[temp[0]][temp[1]-1].prev = [temp[0],temp[1]]
                bfs_queue.append([temp[0],temp[1]-1])
        if temp[1]<9:
            if Map[temp[0]][temp[1]+1].visited=='0':
                Map[temp[0]][temp[1]+1].prev = [temp[0],temp[1]]
                bfs_queue.append([temp[0],temp[1]+1])
        if temp[0]>0:
            if Map[temp[0]-1][temp[1]].visited=='0' :
                Map[temp[0]-1][temp[1]].prev = [temp[0],temp[1]]
                bfs_queue.append([temp[0]-1,temp[1]])
        if temp[0]<9: 
            if Map[temp[0]+1][temp[1]].visited=='0' :
                Map[temp[0]+1][temp[1]].prev = [temp[0],temp[1]] 
                bfs_queue.append([temp[0]+1,temp[1]])
        if temp == finish :
            #print("found")
            PreviousPoint=Map[temp[0]][temp[1]].prev
            while PreviousPoint!=start:
                #print("prevend" + str(Map[PreviousPoint[1]][PreviousPoint[0]].prev))
                Map[PreviousPoint[0]][PreviousPoint[1]].attribute = line_pattern[way_pattern]
                PreviousPoint=Map[PreviousPoint[0]][PreviousPoint[1]].prev 
            #print("end" + str(Map[temp[1]][temp[0]].prev))
            Map[start[0]][start[1]].visited = '1'
            Map[finish[0]][finish[1]].visited = '1'
            #print("execcount = "+str(executeCount))
            return 1
    return 0
def resetvisited(): #reset visited for next pair of point
    for i in range(10):
        for j in range(10):
            if Map[i][j].attribute=="-":
                Map[i][j].visited='0'
def set(Map): #reset map if current pair of point don't make line successfully 
    for i in range(10):
        for j in range(10):
            if Map[i][j].attribute != "x":
                Map[i][j].attribute = "-"
            Map[i][j].visited = '0'

for i in range(10): #set first map
    temp = []
    for j in range(10):
        temp.append(node("-"))
    Map.append(temp)
x= [0,7,2,9,4,1,5,1] # position of point in x-axis (point x[0] is paired of poit x[1])
y= [1,9,1,5,4,5,2,0] # position of point in y-axis (point y[0] is paired of poit y[1])
pair_count = len(x)//2
point_count = len(x)
for i in range(point_count): #mark "x" in map where point exist 
    position = [y[i],x[i]]
    Map[y[i]][x[i]].attribute = 'x'
    Target.append(position)
#print(Target)
way_pattern = 0 #make different line for different pair
success=0 #count number of pair connected successfully
for j in range(pair_count): #bfs for all pair
    for i in range(pair_count): #bfs for each pair
        start = Target.pop(0)
        Target.append(start)
        finish = Target.pop(0) 
        Target.append(finish)
        #print("bfs"+ str(start))
        success+=bfs(start,finish,way_pattern)
        way_pattern+=1
        resetvisited()
    #print(success)
    if success<pair_count and j!=pair_count-1: #reset if all pair aren't connected
        temp = Target.pop(0)
        Target.append(temp)
        temp = Target.pop(0)
        Target.append(temp)
        set(Map)
        way_pattern = 0
        success=0
    else :
        break #end when all pair connected
for i in range(10): #print result
    for j in range(10):
        print(Map[i][j].attribute,end=' ')
    print()
'''for i in range(10):
    for j in range(10):
        print(Map[i][j].visited,end=' ')
    print()'''

