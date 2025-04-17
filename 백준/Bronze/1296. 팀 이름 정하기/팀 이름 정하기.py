yeondoo = input()             # 연두 이름
team_num = int(input())       # 팀 이름 수
name_list = []                # 각 팀 이름 명단

max_p = 0
max_name = ''
for _ in range(team_num):    
    name_list.append(input())

name_list = sorted(name_list) # 리스트를 알파벳 순서로

for name in name_list:        # 각 팀 이름 별로
    teamname = name + yeondoo
    l = teamname.count("L")     # 연두이름이랑 합쳐서 알파벳 갯수 파악
    o = teamname.count("O")
    v = teamname.count("V")
    e = teamname.count("E")
    
    ans = ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e))%100
    if ans == 0:               
        pass
    elif ans > max_p :        
        max_p = ans
        max_name = name				

if max_p == 0:
    print(name_list[0])     
else:
    print(max_name)