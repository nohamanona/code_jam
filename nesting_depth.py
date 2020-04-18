t=int(input())
for i in range(t):
    in_s = input()
    in_s_len = len(in_s)
    out_s = []
    case_num=i+1
    for j in range(in_s_len):
        num = int(in_s[j])
        if j==0:
            num_mae = 0
        else:
            num_mae = int(in_s[j-1])
        #前にかっこ追加
        tmp=in_s[j]
        if num!=num_mae:
            dif=num-num_mae
            if dif>0:
                for k in range(dif):
                    tmp = "("+tmp
            elif dif<0:
                for k in range(abs(dif)):
                    tmp = ")"+tmp
        out_s.append(tmp)
    num=0
    num_mae = int(in_s[in_s_len-1])
    tmp=""
    if num!=num_mae:
        dif=num-num_mae
        if dif>0:
            for k in range(dif):
                tmp = "("+tmp
        elif dif<0:
            for k in range(abs(dif)):
                tmp = ")"+tmp
        out_s.append(tmp)
    ans=""
    for o in range(len(out_s)):
        ans=ans+out_s[o]

    #print("ans",ans)
    print('Case #%d: %s' % (case_num,ans))
