from random import random,randrange

class node :
    def __init__(self,attr,first='',parent='',visited = False,prev=[-1,-1]):
        self.attr = attr
        self.visited = visited
        self.prev = prev
        self.first = first
        self.parent = parent
    def __str__(self):
        return "attr: {0} visited : {1} prev : {2}".format(self.attr,self.visited,self.prev)

Target = [[0,3],[9,4],[2,2],[2,7]]
mapSize = 10
targetNo = 2
Map=[[node('-') for i in range(mapSize)]for i in range(mapSize)]
#[[4, 8], [7, 4], [7, 9], [4, 4], [0, 6], [2, 7], [5, 6], [2, 4]]

def gen_Target(target):
    target_mark=[]
    while len(target_mark)< 2*targetNo:
        temp_point = []
        x=randrange(0,mapSize)
        y=randrange(0,mapSize)
        temp_point.append(x)
        temp_point.append(y)
        if (not temp_point in target_mark):
            target.append(temp_point)
            target_mark.append(temp_point)

def gen_Map(Map,target):
    print(target)
    target_Marker = 'A'
    for i in range(0,2*targetNo,2):
        Map[target[i][0]][target[i][1]] = node(target_Marker)
        Map[target[i+1][0]][target[i+1][1]] = node(target_Marker)
        target_Marker = chr(ord(target_Marker)+1)

def show_Map(Map):
    for i in range(mapSize):
        for j in range(mapSize):
            print(Map[i][j].attr,end=' ')
        print()

def find_color(Map):
    color_list=[]
    for i in range(mapSize):
        for j in range(mapSize):
            if(Map[i][j].attr != '-'):
                color_list.append([i,j])
    color_list=sorted(color_list,key=lambda x: Map[x[0]][x[1]].attr)
    return color_list

def resetVisited(Map):
    for i in range(mapSize):
        for j in range(mapSize):
            if Map[i][j].attr == "-":
                Map[i][j].visited=False

def bidirect_bfs(Map):
    target_list = find_color(Map)
    di_r = [0,0,1,-1]
    di_c = [1,-1,0,0]
    for i in range(0,2*targetNo,2):
        resetVisited(Map)
        q_st = []
        q_en = []
        q_st.append([target_list[i][0],target_list[i][1]])
        q_en.append([target_list[i+1][0],target_list[i+1][1]])
        st_point_i = q_st[0][0]
        st_point_j = q_st[0][1]
        en_point_i = q_en[0][0]
        en_point_j = q_en[0][1]
        Map[st_point_i][st_point_j].first = 'st'
        Map[st_point_i][st_point_j].visited = True
        Map[st_point_i][st_point_j].parent = Map[st_point_i][st_point_j].attr
        Map[en_point_i][en_point_j].first = 'en'
        Map[en_point_i][en_point_j].visited = True
        Map[en_point_i][en_point_j].parent = Map[en_point_i][en_point_j].attr
        while(len(q_st) > 0 or len(q_en) > 0):
            print('bfs')
            #show_Map(Map)

            #start point
            if(len(q_st)>0):
                cur_st_i = q_st[0][0]
                cur_st_j = q_st[0][1]
                q_st.pop(0)
                print('START Q FRONT:',cur_st_i,cur_st_j)
                if(not(cur_st_i == st_point_i and cur_st_j  == st_point_j)):
                    #Map[cur_st_i][cur_st_j].attr = Map[Map[cur_st_i][cur_st_j].prev[0]][Map[cur_st_i][cur_st_j].prev[1]].attr
                    Map[cur_st_i][cur_st_j].parent = Map[Map[cur_st_i][cur_st_j].prev[0]][Map[cur_st_i][cur_st_j].prev[1]].parent
                    Map[cur_st_i][cur_st_j].first = Map[Map[cur_st_i][cur_st_j].prev[0]][Map[cur_st_i][cur_st_j].prev[1]].first
                
                for i in range (4):
                    nst_i = cur_st_i+di_r[i]
                    nst_j = cur_st_j+di_c[i]
                    if(nst_i < 0 or nst_i >= mapSize or nst_j < 0 or nst_j >=mapSize or Map[nst_i][nst_j].attr != '-'):
                        continue
                    if(Map[nst_i][nst_j].visited):
                        if (Map[cur_st_i][cur_st_j].parent == Map[nst_i][nst_j].parent and Map[cur_st_i][cur_st_j].first != Map[nst_i][nst_j].first):
                            print('found')
                            print('at :',nst_i,nst_j)
                            while(not len(q_st)<=0):
                                q_st.pop()
                            while(not len(q_en)<=0):
                                q_en.pop()
                            if([nst_i,nst_j] == [en_point_i,en_point_j]):
                                break;
                            Map[nst_i][nst_j].attr = str.lower(Map[nst_i][nst_j].parent)
                            previ=cur_st_i
                            prevj=cur_st_j
                            while([previ,prevj] != [st_point_i,st_point_j]):
                                if([previ,prevj] == [-1,-1] or [previ,prevj] == [en_point_i,en_point_j]):
                                    break;
                                Map[previ][prevj].attr =  str.lower(Map[nst_i][nst_j].parent)
                                previ_temp=Map[previ][prevj].prev[0]
                                prevj_temp=Map[previ][prevj].prev[1]
                                previ=previ_temp
                                prevj=prevj_temp
                            previ = Map[nst_i][nst_j].prev[0]
                            prevj = Map[nst_i][nst_j].prev[1]
                            while([previ,prevj] != [en_point_i,en_point_j]):
                                if([previ,prevj] == [-1,-1] or [previ,prevj] == [en_point_i,en_point_j]):
                                    break;
                                Map[previ][prevj].attr = str.lower(Map[nst_i][nst_j].parent)
                                previ_temp=Map[previ][prevj].prev[0]
                                prevj_temp=Map[previ][prevj].prev[1]
                                previ=previ_temp
                                prevj=prevj_temp
                            break
                        continue
                    Map[nst_i][nst_j].prev = [cur_st_i,cur_st_j] 
                    Map[nst_i][nst_j].visited = True
                    q_st.append([nst_i,nst_j])

            #end point
            if(len(q_en)>0):
                cur_en_i = q_en[0][0]
                cur_en_j = q_en[0][1]
                q_en.pop(0)
                print('END Q FRONT:',cur_en_i,cur_en_j)
                if(not (cur_en_i == en_point_i and cur_en_j  == en_point_j)):
                    #Map[cur_en_i][cur_en_j].attr = Map[Map[cur_en_i][cur_en_j].prev[0]][Map[cur_en_i][cur_en_j].prev[1]].attr
                    Map[cur_en_i][cur_en_j].parent = Map[Map[cur_en_i][cur_en_j].prev[0]][Map[cur_en_i][cur_en_j].prev[1]].parent
                    Map[cur_en_i][cur_en_j].first = Map[Map[cur_en_i][cur_en_j].prev[0]][Map[cur_en_i][cur_en_j].prev[1]].first
                for i in range (4):
                    nst_i = cur_en_i+di_r[i]
                    nst_j = cur_en_j+di_c[i]
                    if(nst_i < 0 or nst_i >= mapSize or nst_j < 0 or nst_j >=mapSize or Map[nst_i][nst_j].attr != '-'):
                        continue
                    if(Map[nst_i][nst_j].visited):
                        if (Map[cur_en_i][cur_en_j].parent == Map[nst_i][nst_j].parent and Map[cur_en_i][cur_en_j].first != Map[nst_i][nst_j].first):
                            print('found')
                            print('at :',nst_i,nst_j)
                            while(not len(q_st)<=0):
                                q_st.pop()
                            while(not len(q_en)<=0):
                                q_en.pop()
                            if([nst_i,nst_j] == [st_point_i,st_point_j]):
                                break;
                            Map[nst_i][nst_j].attr = str.lower(Map[nst_i][nst_j].parent)
                            previ = Map[nst_i][nst_j].prev[0]
                            prevj = Map[nst_i][nst_j].prev[1]
                            while([previ,prevj] != [st_point_i,st_point_j]):
                                if([previ,prevj] == [-1,-1] or [previ,prevj] == [st_point_i,st_point_j]):
                                    break;
                                Map[previ][prevj].attr = str.lower(Map[nst_i][nst_j].parent)
                                previ_temp=Map[previ][prevj].prev[0]
                                prevj_temp=Map[previ][prevj].prev[1]
                                previ=previ_temp
                                prevj=prevj_temp
                            previ=cur_en_i
                            prevj=cur_en_j
                            while([previ,prevj] != [en_point_i,en_point_j]):
                                if([previ,prevj] == [-1,-1] or [previ,prevj] == [st_point_i,st_point_j]):
                                    break;
                                Map[previ][prevj].attr = str.lower(Map[nst_i][nst_j].parent)
                                previ_temp=Map[previ][prevj].prev[0]
                                prevj_temp=Map[previ][prevj].prev[1]
                                previ=previ_temp
                                prevj=prevj_temp
                            break
                        continue
                    Map[nst_i][nst_j].prev = [cur_en_i,cur_en_j] 
                    Map[nst_i][nst_j].visited = True
                    q_en.append([nst_i,nst_j])


#gen_Target(Target)
gen_Map(Map,Target)
show_Map(Map)
bidirect_bfs(Map)
print('######################')
show_Map(Map)