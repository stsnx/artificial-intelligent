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
    
    #
    finish = findnodepoint(pair_,pair_[0])
    print("finish "+str(finish))
    print("select "+str(point_selection)) 
    while(not finish):
        temp = point_selection.pop(0)
        finish = findnodepoint(pair_,temp)
        
def findnodepoint(pair,currentposition):
    print("find"+str( pair[1])+str( currentposition))
    temp_position = currentposition
    print(str(temp_position))
    if pair[1][1]>=currentposition[1]: #right
        print("r")
        temp_position = currentposition.copy()
        print("current"+str(currentposition))
        found = False
        for i in range(currentposition[1]+1,pair[1][1]):
            print('rr')
            if Map[temp_position[0]][temp_position[1]+1].visited==True:
                Map[temp_position[0]][temp_position[1]+1].attribute='O'
                found==True
                point_selection.append([temp_position[0],temp_position[1]+1])
            temp_position[1]+=1
        
        if not found:
            temp_position[1]+=1
            if temp_position==pair[1]:
                Map[temp_position[0]][temp_position[1]].prev = currentposition
                print("foundr")
                finalposition = temp_position.copy()
                print("final"+ str(finalposition))
                while(finalposition!=[-1,-1]):
                    if Map[finalposition[0]][finalposition[1]].attribute == 'O':
                        Map[finalposition[0]][finalposition[1]].attribute = line_pattern[pattern_position]
                    postfinalposition = Map[finalposition[0]][finalposition[1]].prev.copy()
                    print("postfinal"+ str(postfinalposition))
                    if postfinalposition[0]==finalposition[0]:
                        print('samey')
                        if postfinalposition[1]>finalposition[1]:
                            for i in range (finalposition[1]+1,postfinalposition[1]):
                                Map[finalposition[0]][i].attribute = line_pattern[pattern_position]
                                Map[finalposition[0]][i].visited = True
                        else :
                            for i in range (postfinalposition[1]+1,finalposition[1]):
                                Map[finalposition[0]][i].attribute = line_pattern[pattern_position]
                                Map[finalposition[0]][i].visited = True
                    if postfinalposition[1]==finalposition[1]:
                        print('samex')
                        if postfinalposition[0]>finalposition[0]:
                            for i in range (finalposition[0]+1,postfinalposition[0]):
                                Map[i][finalposition[1]].attribute = line_pattern[pattern_position]
                                Map[i][finalposition[1]].visited = True
                        else :
                            for i in range (postfinalposition[0]+1,finalposition[0]):
                                Map[i][finalposition[1]].attribute = line_pattern[pattern_position]
                                Map[i][finalposition[1]].visited = True
                    finalposition = postfinalposition
                return True
            else:
                if(Map[temp_position[0]][temp_position[1]].visited==False):
                    Map[temp_position[0]][temp_position[1]].attribute='O'
                    Map[temp_position[0]][temp_position[1]].prev = currentposition
                    Map[temp_position[0]][temp_position[1]].distance= temp_position[1] - currentposition[1]
                    point_selection.append(temp_position)
                   


    if pair[1][1]<currentposition[1]: #left
        print("l")
        temp_position = currentposition.copy()
        print("current"+str(currentposition))
        found = False
        for i in range(currentposition[1]-1,pair[1][1],-1):
            print('ll')
            if Map[temp_position[0]][temp_position[1]-1].visited==True:
                Map[temp_position[0]][temp_position[1]-1].attribute='O'
                found==True
                point_selection.append([temp_position[0],temp_position[1]-1])
            temp_position[1]-=1
        
        if not found:
            temp_position[1]-=1
            if temp_position==pair[1]:
                Map[temp_position[0]][temp_position[1]].prev = currentposition
                print("foundl")
                finalposition = temp_position.copy()
                print("final"+ str(finalposition))
                while(finalposition!=[-1,-1]):
                    if Map[finalposition[0]][finalposition[1]].attribute == 'O':
                        Map[finalposition[0]][finalposition[1]].attribute = line_pattern[pattern_position]
                    postfinalposition = Map[finalposition[0]][finalposition[1]].prev.copy()
                    print("postfinal"+ str(postfinalposition))
                    if postfinalposition[0]==finalposition[0]:
                        print('samey')
                        if postfinalposition[1]>finalposition[1]:
                            for i in range (finalposition[1]+1,postfinalposition[1]):
                                Map[finalposition[0]][i].attribute = line_pattern[pattern_position]
                                Map[finalposition[0]][i].visited = True
                        else :
                            for i in range (postfinalposition[1]+1,finalposition[1]):
                                Map[finalposition[0]][i].attribute = line_pattern[pattern_position]
                                Map[finalposition[0]][i].visited = True
                    if postfinalposition[1]==finalposition[1]:
                        print('samex')
                        if postfinalposition[0]>finalposition[0]:
                            for i in range (finalposition[0]+1,postfinalposition[0]):
                                Map[i][finalposition[1]].attribute = line_pattern[pattern_position]
                                Map[i][finalposition[1]].visited = True
                        else :
                            for i in range (postfinalposition[0]+1,finalposition[0]):
                                Map[i][finalposition[1]].attribute = line_pattern[pattern_position]
                                Map[i][finalposition[1]].visited = True
                    finalposition = postfinalposition
                return True
            else:
                if(Map[temp_position[0]][temp_position[1]].visited==False):
                    Map[temp_position[0]][temp_position[1]].attribute='O'
                    Map[temp_position[0]][temp_position[1]].prev = currentposition
                    Map[temp_position[0]][temp_position[1]].distance= temp_position[1] - currentposition[1]
                    point_selection.append(temp_position)
                    
    if pair[1][0]>=currentposition[0]: #down
        print("d")
        temp_position = currentposition.copy()
        print("current"+str(currentposition))
        found = False
        for i in range(currentposition[0]+1,pair[1][0]):
            print('dd')
            if Map[temp_position[0]+1][temp_position[1]].visited==True:
                Map[temp_position[0]+1][temp_position[1]].attribute='O'
                found==True
                point_selection.append([temp_position[0]+1,temp_position[1]])
            temp_position[0]+=1
        
        if not found:
            temp_position[0]+=1
            if temp_position==pair[1]:
                Map[temp_position[0]][temp_position[1]].prev = currentposition
                print("foundd")
                finalposition = temp_position.copy()
                print("final"+ str(finalposition))
                while(finalposition!=[-1,-1]):
                    if Map[finalposition[0]][finalposition[1]].attribute == 'O':
                        Map[finalposition[0]][finalposition[1]].attribute = line_pattern[pattern_position]
                    postfinalposition = Map[finalposition[0]][finalposition[1]].prev.copy()
                    print("postfinal"+ str(postfinalposition))
                    if postfinalposition[0]==finalposition[0]:
                        print('samey')
                        if postfinalposition[1]>finalposition[1]:
                            for i in range (finalposition[1]+1,postfinalposition[1]):
                                Map[finalposition[0]][i].attribute = line_pattern[pattern_position]
                                Map[finalposition[0]][i].visited = True
                        else :
                            for i in range (postfinalposition[1]+1,finalposition[1]):
                                Map[finalposition[0]][i].attribute = line_pattern[pattern_position]
                                Map[finalposition[0]][i].visited = True
                    if postfinalposition[1]==finalposition[1]:
                        print('samex')
                        if postfinalposition[0]>finalposition[0]:
                            for i in range (finalposition[0]+1,postfinalposition[0]):
                                Map[i][finalposition[1]].attribute = line_pattern[pattern_position]
                                Map[i][finalposition[1]].visited = True
                        else :
                            for i in range (postfinalposition[0]+1,finalposition[0]):
                                Map[i][finalposition[1]].attribute = line_pattern[pattern_position]
                                Map[i][finalposition[1]].visited = True
                    finalposition = postfinalposition
                return True
            else:
                if(Map[temp_position[0]][temp_position[1]].visited==False):
                    Map[temp_position[0]][temp_position[1]].attribute='O'
                    Map[temp_position[0]][temp_position[1]].prev = currentposition
                    Map[temp_position[0]][temp_position[1]].distance= temp_position[0] - currentposition[0]
                    point_selection.append(temp_position)
                    
    if pair[1][0]<currentposition[0]: #up
        print("u")
        temp_position = currentposition.copy()
        print("current"+str(currentposition))
        found = False
        for i in range(currentposition[0]-1,pair[1][0],-1):
            print("b"+str(temp_position))
            print('uu')
            if Map[temp_position[0]-1][temp_position[1]].visited==True:
                print("drawO")
                Map[temp_position[0]-1][temp_position[1]].attribute='O'
                found==True
                point_selection.append([temp_position[0]-1,temp_position[1]])
            temp_position[0]-=1
            print("a"+str(temp_position))
        if not found: 
            temp_position[0]-=1
            if temp_position==pair[1]:
                Map[temp_position[0]][temp_position[1]].prev = currentposition
                print("foundu")
                finalposition = temp_position.copy()
                print("final"+ str(finalposition))
                while(finalposition!=[-1,-1]):
                    if Map[finalposition[0]][finalposition[1]].attribute == 'O':
                        Map[finalposition[0]][finalposition[1]].attribute = line_pattern[pattern_position]
                    postfinalposition = Map[finalposition[0]][finalposition[1]].prev.copy()
                    print("postfinal"+ str(postfinalposition))
                    if postfinalposition[0]==finalposition[0]:
                        print('samey')
                        if postfinalposition[1]>finalposition[1]:
                            for i in range (finalposition[1]+1,postfinalposition[1]):
                                Map[finalposition[0]][i].attribute = line_pattern[pattern_position]
                                Map[finalposition[0]][i].visited = True
                        else :
                            for i in range (postfinalposition[1]+1,finalposition[1]):
                                Map[finalposition[0]][i].attribute = line_pattern[pattern_position]
                                Map[finalposition[0]][i].visited = True
                    if postfinalposition[1]==finalposition[1]:
                        print('samex')
                        if postfinalposition[0]>finalposition[0]:
                            for i in range (finalposition[0]+1,postfinalposition[0]):
                                Map[i][finalposition[1]].attribute = line_pattern[pattern_position]
                                Map[i][finalposition[1]].visited = True
                        else :
                            for i in range (postfinalposition[0]+1,finalposition[0]):
                                Map[i][finalposition[1]].attribute = line_pattern[pattern_position]
                                Map[i][finalposition[1]].visited = True
                    finalposition = postfinalposition
                return True
            else:
                if(Map[temp_position[0]][temp_position[1]].visited==False):
                    Map[temp_position[0]][temp_position[1]].attribute='O'
                    Map[temp_position[0]][temp_position[1]].prev = currentposition
                    Map[temp_position[0]][temp_position[1]].distance= temp_position[0] - currentposition[0]
                    point_selection.append(temp_position)
                    
    #make decition before
    print(str(Map[pair[1][0]][pair[1][1]]))
    return False
    
'''print(str(quick_sum_horizontal))
            if quick_sum_horizontal[pair[1][1]]-quick_sum_horizontal[pair[0][1]]<=1:
                if currentposition == pair[1]:
                    Map[pair[1][0]][pair[1][1]].prev = currentposition
                    print("found")
                    return True
'''

#x= [6,3,3,0,5,7,2,5] # position of point in x-axis (point x[0] is paired of poit x[1])
#y= [7,7,0,6,0,6,0,5] # position of point in y-axis (point y[0] is paired of poit y[1])
x=[3,8]
y=[7,2]
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
pair_set = sort_by_distance(pair_set)
for i in range (1):
    local_beam_search(pair_set[i])
for i in range(10): #print result
    for j in range(10):
        print(Map[i][j].attribute,end=' ')
    print()
