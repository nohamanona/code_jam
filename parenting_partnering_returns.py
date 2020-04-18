t=int(input())
for i in range(t):
    case_num = i+1
    active_num = 0
    n=int(input())
    schedule_list = []
    ans_list=[""for a in range(n)]
    #print("ans_l",ans_list)
    possible = True
    ans=""
    j_active_flg=-1
    for j in range(n):
        schedule_list.append(list(map(int,input().split())))
    #print(schedule_list)
    for time in range(24*60+1):
        for k in range(n):
            if time == schedule_list[k][1]:
                active_num=active_num-1
                if j_active_flg==k:
                    j_active_flg=-1
        for k in range(n):
            if time == schedule_list[k][0]:
                if active_num ==0:
                    ans_list[k]='C'
                    #print("time=",time,"sche=",k,"add C")
                elif (active_num == 1) and (j_active_flg == -1):
                    ans_list[k]='J'
                    j_active_flg=k
                    #print("time=",time,"sche=",k,"add J")
                elif (active_num == 1) and (j_active_flg != -1):
                    ans_list[k]='C'
                    #print("time=",time,"sche=",k,"add C J active")
                elif active_num>=2:
                    possible = False
                    break
                active_num+=1
            
        if possible==False:
            break
    if possible:
        for o in range(len(ans_list)):
            ans =ans+ans_list[o]
    else:
        ans = "IMPOSSIBLE"
    #print("ans",ans)
    print('Case #%d: %s' % (case_num,ans))


