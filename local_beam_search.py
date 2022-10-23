from random import random, randrange
from itertools import permutations
from re import search 
import time
import os, psutil
import tracemalloc
class node: #node structure of each point in map
    def __init__(self,attribute,previous=[-1,-1],distance =0) :
        self.attribute = attribute
        self.prev = previous
        self.distance = distance
        self.visited = False
Map = []
pair_set=[]
point_selection = []
line_pattern = "|\+!%^"
pattern_position = 0
line_path = []
def sort_by_distance(pair_Set):
    sorted_pair = []
    current_distance = abs(pair_Set[0][0][0]-pair_Set[0][1][0])+abs(pair_Set[0][0][1]-pair_Set[0][1][1])
    pair_set[0].append(current_distance)
    sorted_pair.append(pair_set[0])
    for i in range (1,len(pair_Set)):
        new_distance = abs(pair_Set[i][0][0]-pair_Set[i][1][0])+abs(pair_Set[i][0][1]-pair_Set[i][1][1])
        pair_set[i].append(new_distance)
        if new_distance >= current_distance:
            sorted_pair.append(pair_set[i])
            current_distance = new_distance
        else :
            for j in range (len(sorted_pair)-1,-1,-1):
                if sorted_pair[j][2] < new_distance :
                    sorted_pair.insert(j+1, pair_set[i])
    return sorted_pair
def local_beam_search(pair_):
    finish = findnodepoint(pair_,pair_[0])
    #print("finish "+str(finish))
    #print("select "+str(point_selection)) 
    while(not finish):
        temp = point_selection.pop(0)
        finish = findnodepoint(pair_,temp)
        if point_selection == []:
            break
    return finish
        
def findnodepoint(pair,currentposition):
    #print("find"+str( pair[1])+str( currentposition))
    temp_position = currentposition
    #print(str(temp_position))
    if pair[1][1]>=currentposition[1]: #right
        temp_position = currentposition.copy()
       # print("currentr"+str(currentposition))
        found = False
        if Map[temp_position[0]][temp_position[1]+1].visited==True:
            found = True 
        for i in range(currentposition[1]+1,pair[1][1]):
            if Map[temp_position[0]][temp_position[1]+1].visited==True and temp_position!=currentposition:
                
                if not Map[temp_position[0]][temp_position[1]].attribute.isalpha():
                    Map[temp_position[0]][temp_position[1]].attribute='O'
                    found=True
                 #   print("will append" +str(temp_position[0])+ str(temp_position[1]) + str(Map[temp_position[0]][temp_position[1]].attribute)+str(Map[temp_position[0]][temp_position[1]].visited))
                 #   print('append1')
                    point_selection.append([temp_position[0],temp_position[1]])
                if Map[temp_position[0]][temp_position[1]].attribute.isalpha() and Map[temp_position[0]][temp_position[1]].attribute==Map[pair[1][0]][pair[1][1]].attribute:
                    found = True
            temp_position[1]+=1
        #print("found?  = " + str(found))
        if not found:
            temp_position[1]+=1
            if temp_position==pair[1]:
                Map[temp_position[0]][temp_position[1]].prev = currentposition
             #   print("foundr")
                finalposition = temp_position.copy()
             #   print("final"+ str(finalposition))
                path = []
                
                while(finalposition!=[-1,-1]):
                    path.append(finalposition)
                    if Map[finalposition[0]][finalposition[1]].attribute == 'O':
                        Map[finalposition[0]][finalposition[1]].attribute = line_pattern[pattern_position]
                        path.append(finalposition)
                    postfinalposition = Map[finalposition[0]][finalposition[1]].prev.copy()
                 #   print("postfinal"+ str(postfinalposition))
                    if postfinalposition[0]==finalposition[0]:
                 #       print('samey')
                        if postfinalposition[1]>finalposition[1]:
                            for i in range (finalposition[1]+1,postfinalposition[1]):
                                Map[finalposition[0]][i].attribute = line_pattern[pattern_position]
                                Map[finalposition[0]][i].visited = True
                                resposition = [finalposition[0],i]
                                path.append(resposition)
                        else :
                            for i in range (postfinalposition[1]+1,finalposition[1]):
                                Map[finalposition[0]][i].attribute = line_pattern[pattern_position]
                                Map[finalposition[0]][i].visited = True
                                resposition = [finalposition[0],i]
                                path.append(resposition)
                    if postfinalposition[1]==finalposition[1]:
                     #   print('samex')
                        if postfinalposition[0]>finalposition[0]:
                            for i in range (finalposition[0]+1,postfinalposition[0]):
                                Map[i][finalposition[1]].attribute = line_pattern[pattern_position]
                                Map[i][finalposition[1]].visited = True
                                resposition = [i,finalposition[1]]
                                path.append(resposition)
                        else :
                            for i in range (postfinalposition[0]+1,finalposition[0]):
                       #         print(str("chevk")+str(i) + str(line_pattern[pattern_position]))
                                Map[i][finalposition[1]].attribute = line_pattern[pattern_position]
                                Map[i][finalposition[1]].visited = True
                                resposition = [i,finalposition[1]]
                                path.append(resposition)
                    finalposition = postfinalposition
                line_path.append(path)
                return True
            else:
              #  print("will append" +str(temp_position[0])+ str(temp_position[1]) + str(Map[temp_position[0]][temp_position[1]].attribute)+str(Map[temp_position[0]][temp_position[1]].visited))
                if(Map[temp_position[0]][temp_position[1]].visited==False):
                    Map[temp_position[0]][temp_position[1]].attribute='O'
                    Map[temp_position[0]][temp_position[1]].prev = currentposition
                    Map[temp_position[0]][temp_position[1]].distance= temp_position[1] - currentposition[1]
                  #  print('append2')
                    point_selection.append(temp_position)
                   
    if pair[1][1]<currentposition[1]: #left
        temp_position = currentposition.copy()
      #  print("currentl"+str(currentposition))
        found = False
        if Map[temp_position[0]][temp_position[1]-1].visited==True:
            found = True 
        for i in range(currentposition[1]-1,pair[1][1],-1):
           # print(i)
          #  print("now in"+ str(temp_position[0])+ str(temp_position[1]))
           # print("next "+ str(temp_position[0])+ str(temp_position[1]-1)+ " is " + str(Map[temp_position[0]][temp_position[1]-1].attribute)+ str(Map[temp_position[0]][temp_position[1]-1].visited))
            if Map[temp_position[0]][temp_position[1]-1].visited==True and temp_position!=currentposition:
                
             #   print("now on"+ str(temp_position[0])+ str(temp_position[1]))
                if not Map[temp_position[0]][temp_position[1]-1].attribute.isalpha() and Map[temp_position[0]][temp_position[1]-1].attribute != '-':
                    found=True
                if not Map[temp_position[0]][temp_position[1]].attribute.isalpha():
                    Map[temp_position[0]][temp_position[1]].attribute='O'
                    found=True
                 #   print("will append" +str(temp_position[0])+ str(temp_position[1]) + str(Map[temp_position[0]][temp_position[1]].attribute)+str(Map[temp_position[0]][temp_position[1]].visited))
                 #   print('append1')
                    point_selection.append([temp_position[0],temp_position[1]])
                if Map[temp_position[0]][temp_position[1]].attribute.isalpha() and Map[temp_position[0]][temp_position[1]].attribute==Map[pair[1][0]][pair[1][1]].attribute:
                    found = True
                
            temp_position[1]-=1
       # print("found?  = " + str(found))
        if not found:
            temp_position[1]-=1
            if temp_position==pair[1]:
                Map[temp_position[0]][temp_position[1]].prev = currentposition
            #    print("foundl")
                finalposition = temp_position.copy()
            #    print("final"+ str(finalposition))
                path = []
                while(finalposition!=[-1,-1]):
                    path.append(finalposition)
                    if Map[finalposition[0]][finalposition[1]].attribute == 'O':
                        Map[finalposition[0]][finalposition[1]].attribute = line_pattern[pattern_position]
                    postfinalposition = Map[finalposition[0]][finalposition[1]].prev.copy()
            #        print("postfinal"+ str(postfinalposition))
                    if postfinalposition[0]==finalposition[0]:
            #            print('samey')
                        if postfinalposition[1]>finalposition[1]:
                            for i in range (finalposition[1]+1,postfinalposition[1]):
                                Map[finalposition[0]][i].attribute = line_pattern[pattern_position]
                                Map[finalposition[0]][i].visited = True
                                resposition = [finalposition[0],i]
                                path.append(resposition)
                        else :
                            for i in range (postfinalposition[1]+1,finalposition[1]):
                                Map[finalposition[0]][i].attribute = line_pattern[pattern_position]
                                Map[finalposition[0]][i].visited = True
                                resposition = [finalposition[0],i]
                                path.append(resposition)
                    if postfinalposition[1]==finalposition[1]:
            #            print('samex')
                        if postfinalposition[0]>finalposition[0]:
                            for i in range (finalposition[0]+1,postfinalposition[0]):
                                Map[i][finalposition[1]].attribute = line_pattern[pattern_position]
                                Map[i][finalposition[1]].visited = True
                                resposition = [i,finalposition[1]]
                                path.append(resposition)
                        else :
                            for i in range (postfinalposition[0]+1,finalposition[0]):
                                Map[i][finalposition[1]].attribute = line_pattern[pattern_position]
                                Map[i][finalposition[1]].visited = True
                                resposition = [i,finalposition[1]]
                                path.append(resposition)
                    finalposition = postfinalposition
                line_path.append(path)
                return True
            else:
            #    print("will append" +str(temp_position[0])+ str(temp_position[1]) + str(Map[temp_position[0]][temp_position[1]].attribute)+str(Map[temp_position[0]][temp_position[1]].visited))
                if(Map[temp_position[0]][temp_position[1]].visited==False):
                    Map[temp_position[0]][temp_position[1]].attribute='O'
                    Map[temp_position[0]][temp_position[1]].prev = currentposition
                    Map[temp_position[0]][temp_position[1]].distance= temp_position[1] - currentposition[1]
            #        print('append2')
                    point_selection.append(temp_position)
                    
    if pair[1][0]>=currentposition[0]: #down
        temp_position = currentposition.copy()
    #    print("currentd"+str(currentposition))
        found = False
        if Map[temp_position[0]+1][temp_position[1]].visited==True:
            found = True 
        for i in range(currentposition[0]+1,pair[1][0]):
            if Map[temp_position[0]+1][temp_position[1]].visited==True and temp_position!=currentposition:
               
                Map[temp_position[0]][temp_position[1]].attribute='O'
                found=True
    #            print("will append" +str(temp_position[0])+ str(temp_position[1]) + str(Map[temp_position[0]][temp_position[1]].attribute)+str(Map[temp_position[0]][temp_position[1]].visited))
    #            print('append1')
                point_selection.append([temp_position[0],temp_position[1]])
            temp_position[0]+=1
        
        if not found:
            temp_position[0]+=1
            if temp_position==pair[1]:
                Map[temp_position[0]][temp_position[1]].prev = currentposition
    #            print("foundd")
                finalposition = temp_position.copy()
    #            print("final"+ str(finalposition))
                path = []
                while(finalposition!=[-1,-1]):
                    path.append(finalposition)
                    if Map[finalposition[0]][finalposition[1]].attribute == 'O':
                        Map[finalposition[0]][finalposition[1]].attribute = line_pattern[pattern_position]
                    postfinalposition = Map[finalposition[0]][finalposition[1]].prev.copy()
    #                print("postfinal"+ str(postfinalposition))
                    if postfinalposition[0]==finalposition[0]:
    #                    print('samey')
                        if postfinalposition[1]>finalposition[1]:
                            for i in range (finalposition[1]+1,postfinalposition[1]):
                                Map[finalposition[0]][i].attribute = line_pattern[pattern_position]
                                Map[finalposition[0]][i].visited = True
                                resposition = [finalposition[0],i]
                                path.append(resposition)
                        else :
                            for i in range (postfinalposition[1]+1,finalposition[1]):
                                Map[finalposition[0]][i].attribute = line_pattern[pattern_position]
                                Map[finalposition[0]][i].visited = True
                                resposition = [finalposition[0],i]
                                path.append(resposition)
                    if postfinalposition[1]==finalposition[1]:
    #                    print('samex')
                        if postfinalposition[0]>finalposition[0]:
                            for i in range (finalposition[0]+1,postfinalposition[0]):
                                Map[i][finalposition[1]].attribute = line_pattern[pattern_position]
                                Map[i][finalposition[1]].visited = True
                                resposition = [i,finalposition[1]]
                                path.append(resposition)
                        else :
                            for i in range (postfinalposition[0]+1,finalposition[0]):
                                Map[i][finalposition[1]].attribute = line_pattern[pattern_position]
                                Map[i][finalposition[1]].visited = True
                                resposition = [i,finalposition[1]]
                                path.append(resposition)
                    finalposition = postfinalposition
                line_path.append(path)
                return True
            else:
    #            print("will append" +str(temp_position[0])+ str(temp_position[1]) + str(Map[temp_position[0]][temp_position[1]].attribute)+str(Map[temp_position[0]][temp_position[1]].visited))
                if(Map[temp_position[0]][temp_position[1]].visited==False):
                    Map[temp_position[0]][temp_position[1]].attribute='O'
                    Map[temp_position[0]][temp_position[1]].prev = currentposition
                    Map[temp_position[0]][temp_position[1]].distance= temp_position[0] - currentposition[0]
    #                print('append2')
                    point_selection.append(temp_position)
                    
    if pair[1][0]<currentposition[0]: #up
        temp_position = currentposition.copy()
    #    print("currentu"+str(currentposition))
        found = False
        if Map[temp_position[0]-1][temp_position[1]].visited==True:
            found = True 
        for i in range(currentposition[0]-1,pair[1][0],-1):
    #        print("b"+str(temp_position))
            if Map[temp_position[0]-1][temp_position[1]].visited==True and temp_position!=currentposition:
                
                if not Map[temp_position[0]][temp_position[1]].attribute.isalpha():
                    Map[temp_position[0]][temp_position[1]].attribute='O'
                    found=True
    #                print("will append" +str(temp_position[0])+ str(temp_position[1]) + str(Map[temp_position[0]][temp_position[1]].attribute)+str(Map[temp_position[0]][temp_position[1]].visited))
    #                print('append1')
                    point_selection.append([temp_position[0],temp_position[1]])
                if Map[temp_position[0]][temp_position[1]].attribute.isalpha() and Map[temp_position[0]][temp_position[1]].attribute==Map[pair[1][0]][pair[1][1]].attribute:
                    found = True
            temp_position[0]-=1
    #        print("a"+str(temp_position))
        if not found: 
            temp_position[0]-=1
            if temp_position==pair[1]:
                Map[temp_position[0]][temp_position[1]].prev = currentposition
                finalposition = temp_position.copy()
    #            print("final"+ str(finalposition))
                path = []
                while(finalposition!=[-1,-1]):
                    path.append(finalposition)
                    if Map[finalposition[0]][finalposition[1]].attribute == 'O':
                        Map[finalposition[0]][finalposition[1]].attribute = line_pattern[pattern_position]
                    postfinalposition = Map[finalposition[0]][finalposition[1]].prev.copy()
    #                print("postfinal"+ str(postfinalposition))
                    if postfinalposition[0]==finalposition[0]:
    #                    print('samey')
                        if postfinalposition[1]>finalposition[1]:
                            for i in range (finalposition[1]+1,postfinalposition[1]):
                                Map[finalposition[0]][i].attribute = line_pattern[pattern_position]
                                Map[finalposition[0]][i].visited = True
                                resposition = [finalposition[0],i]
                                path.append(resposition)
                        else :
                            for i in range (postfinalposition[1]+1,finalposition[1]):
                                Map[finalposition[0]][i].attribute = line_pattern[pattern_position]
                                Map[finalposition[0]][i].visited = True
                                resposition = [finalposition[0],i]
                                path.append(resposition)
                    if postfinalposition[1]==finalposition[1]:
    #                    print('samex')
                        if postfinalposition[0]>finalposition[0]:
                            for i in range (finalposition[0]+1,postfinalposition[0]):
                                Map[i][finalposition[1]].attribute = line_pattern[pattern_position]
                                Map[i][finalposition[1]].visited = True
                                resposition = [i,finalposition[1]]
                                path.append(resposition)
                        else :
                            for i in range (postfinalposition[0]+1,finalposition[0]):
                                Map[i][finalposition[1]].attribute = line_pattern[pattern_position]
                                Map[i][finalposition[1]].visited = True
                                resposition = [i,finalposition[1]]
                                path.append(resposition)
                    finalposition = postfinalposition
                line_path.append(path)
                return True
            else:
    #            print("will append" +str(temp_position[0])+ str(temp_position[1]) + str(Map[temp_position[0]][temp_position[1]].attribute)+str(Map[temp_position[0]][temp_position[1]].visited))
                if(Map[temp_position[0]][temp_position[1]].visited==False):
                    Map[temp_position[0]][temp_position[1]].attribute='O'
                    Map[temp_position[0]][temp_position[1]].prev = currentposition
                    Map[temp_position[0]][temp_position[1]].distance= temp_position[0] - currentposition[0]
    #                print('append2')
                    point_selection.append(temp_position)
                    
    #make decition before
    #print(str(Map[pair[1][0]][pair[1][1]]))
    return False
def resetmarkpoint(Map):
    for i in range(10):
        for j in range(10):
            if Map[i][j].attribute=='O':
                Map[i][j].attribute = "-"
                Map[i][j].prev = []
                Map[i][j].visited = False
def bfs(start,finish,way_pattern): #normal breath first search
    
    bfs_queue = []
    bfs_queue.append(start)
    Map[start[0]][start[1]].visited=True
    Map[finish[0]][finish[1]].visited=False
    Map[start[0]][start[1]].prev=[-1,-1]
    while len(bfs_queue)>0:
        
        temp = bfs_queue.pop(0) #temp is first position in queue for search in bfs
        Map[temp[0]][temp[1]].visited=True
        #if wp==2:
            #print("node"+str(temp)+" prev "+str(Map[temp[0]][temp[1]].prev)+"finish "+str(finish) +" "+ str(Map[finish[0]][finish[1]].visited))
        if temp[1]<9:
            if Map[temp[0]][temp[1]+1].visited==False:
                Map[temp[0]][temp[1]+1].prev = [temp[0],temp[1]]
                if not Map[temp[0]][temp[1]+1].attribute.isalpha():
                    bfs_queue.append([temp[0],temp[1]+1])
                elif temp[0]==finish[0] and temp[1]+1==finish[1]:
                    bfs_queue.append([temp[0],temp[1]+1])
        if temp[1]>0:
            if Map[temp[0]][temp[1]-1].visited==False:
                Map[temp[0]][temp[1]-1].prev = [temp[0],temp[1]]
                if not Map[temp[0]][temp[1]-1].attribute.isalpha():
                    bfs_queue.append([temp[0],temp[1]-1])
                elif temp[0]==finish[0] and temp[1]-1==finish[1]:
                    bfs_queue.append([temp[0],temp[1]-1])
        if temp[0]>0:
            if Map[temp[0]-1][temp[1]].visited==False :
                Map[temp[0]-1][temp[1]].prev = [temp[0],temp[1]]
                if not Map[temp[0]-1][temp[1]].attribute.isalpha():
                    bfs_queue.append([temp[0]-1,temp[1]])
                elif temp[0]-1==finish[0] and temp[1]==finish[1]:
                    bfs_queue.append([temp[0]-1,temp[1]])
        if temp[0]<9: 
            if Map[temp[0]+1][temp[1]].visited==False :
                Map[temp[0]+1][temp[1]].prev = [temp[0],temp[1]] 
                if not Map[temp[0]+1][temp[1]].attribute.isalpha():
                    bfs_queue.append([temp[0]+1,temp[1]])
                elif temp[0]==finish[0] and temp[1]+1==finish[1]:
                    bfs_queue.append([temp[0]+1,temp[1]])
        
        
        
        path = []
        if temp == finish :
            #print("found")
            path.append(finish)
            PreviousPoint=Map[temp[0]][temp[1]].prev
            while PreviousPoint!=start:
                path.append(PreviousPoint)
                #print("prevend" + str(Map[PreviousPoint[1]][PreviousPoint[0]].prev))
                Map[PreviousPoint[0]][PreviousPoint[1]].attribute = line_pattern[way_pattern]
                PreviousPoint=Map[PreviousPoint[0]][PreviousPoint[1]].prev 
            #print("end" + str(Map[temp[1]][temp[0]].prev))
            Map[start[0]][start[1]].visited = True
            Map[finish[0]][finish[1]].visited = True
            path.append(start)
            line_path.append(path)
            #print("execcount = "+str(executeCount))
            return 1
    return 0   


'''print(str(quick_sum_horizontal))
            if quick_sum_horizontal[pair[1][1]]-quick_sum_horizontal[pair[0][1]]<=1:
                if currentposition == pair[1]:
                    Map[pair[1][0]][pair[1][1]].prev = currentposition
                    print("found")
                    return True
'''

#x= [6,3,3,0,5,7,2,5] # position of point in x-axis (point x[0] is paired of poit x[1])
#y= [7,7,0,6,0,6,0,5] # position of point in y-axis (point y[0] is paired of poit y[1])
x=[6,3,5,0,5,7,2,5]
y=[7,7,2,6,0,6,0,5]
for i in range(10): #set first map
    temp = []
    for j in range(10):
        temp.append(node("-"))
    Map.append(temp)
point_count = len(x)
Map_Marker = 'A'
pair_temp = []
for i in range(point_count): #mark "x" in map where point exist 
    position = [y[i],x[i]]
    pair_temp.append(position)
    Map[y[i]][x[i]].attribute = chr(ord(Map_Marker)+(i//2))
    Map[y[i]][x[i]].visited = True
    if i%2==1:
        pair_set.append(pair_temp)
        pair_temp=[]
print(str(pair_set))
start_time = int(round(time.time()*1000))
tracemalloc.start()
pair_set = sort_by_distance(pair_set)

for i in range (len(pair_set)):
    res = local_beam_search(pair_set[i])
    if res == False :
        resetmarkpoint(Map)
        x =bfs(pair_set[i][0],pair_set[i][1],pattern_position)
    print("res = "+ str(res))
    resetmarkpoint(Map)
    point_selection = []
    pattern_position+=1
end_time = int(round(time.time()*1000))
for i in range(10): #print result
    for j in range(10):
        print(Map[i][j].attribute,end=' ')
    print()
for i in range(len(pair_set)):
    print("path "+chr(65+i)+ " : "+str(line_path[i]))
print("Searched time used {} millisecond".format(end_time-start_time))
memUsed  = list(tracemalloc .get_traced_memory())

print("Searched memory current used {:,} byte, peak memory usage {:,} byte".format(memUsed[0],memUsed[1]))
tracemalloc.stop()