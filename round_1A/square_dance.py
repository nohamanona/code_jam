import numpy as np
t=int(input())
for i in range(t):
    r,c = map(int,input().split())
    list_s = []
    for j in range(r):
        list_s.append(list(map(int,input().split())))
    #print(r,c,list_s)

    #rc_list[r][c][0]:上方向のcompass neighbor
    #rc_list[r][c][1]:左方向のcompass neighbor
    #rc_list[r][c][2]:自分自身
    #rc_list[r][c][3]:右方向のcompass neighbor
    #rc_list[r][c][4]:下方向のcompass neighbor

    rc_mask = np.zeros((r,c))
    mask_num_tmp = -1
    interest_tmp =0
    ans = 0
    while(1):
        r_list=np.zeros((r,2), dtype=np.int16)
        c_list=np.zeros((c,2), dtype=np.int16)
        rc_list=np.zeros((r,c,5), dtype=np.int16)
        for y in range(r):
            for x in range(c):
                if rc_mask[y][x]:
                    continue
                #上下方向
                #c_list[x][0]の値をrc_listの[y][x][0]に格納
                #c_list[x][1]の列数を読み、rc_listの[その列数][x][4]に自分自身のスキル値をいれる
                #c_listを上と同様に更新
                rc_list[y][x][0]=c_list[x][0]
                if c_list[x][1] !=0:
                    rc_list[c_list[x][1]-1][x][4]=list_s[y][x]
                c_list[x][0] = list_s[y][x]
                c_list[x][1] = y+1

                rc_list[y][x][2] = list_s[y][x]

                #左右も同様
                rc_list[y][x][1] = r_list[y][0]
                if r_list[y][1] !=0:
                    rc_list[y][r_list[y][1]-1][3] = list_s[y][x]
                r_list[y][0] = list_s[y][x]
                r_list[y][1] = x+1
        #print("rc_list= ",rc_list)
        interest = 0
        for y in range(r):
            for x in range(c):
                total = 0
                num = 0
                ave = 0
                if rc_mask[y][x]:
                    continue
                for a in range(5):
                    if rc_list[y][x][a]==0:
                        continue
                    if a==2:
                        continue
                    total += rc_list[y][x][a]
                    num += 1
                if num==0:
                    ave=total
                else:
                    ave = total/num

                if rc_list[y][x][2] < ave:
                    rc_mask[y][x]=1

                interest += rc_list[y][x][2]
        #print("interest=",interest)
        mask_num = np.sum(rc_mask)
        #print("mask_num,masknum_tmp=",mask_num,mask_num_tmp)
        if interest ==interest_tmp:
            break

        interest_tmp = interest
        mask_num_tmp = mask_num
        ans = ans + interest
    case_num=i+1
    print('Case #%d: %s' % (case_num,ans))

    
            






