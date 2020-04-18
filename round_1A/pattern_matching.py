t=int(input())
for i in range(t):
    n=int(input())
    p = []
    max_str=0
    max_str_no=0
    total_str=0
    for j in range(n):
        pj = input()
        p.append(pj)
        if len(pj)>max_str:
            max_str=len(pj)
            max_str_no=j
            total_str=total_str+len(pj)
    #print(p)
    
    read_char_num=[0 * n]
    head_str_num=-1
    head_list=[]
    
    for l in range(n):
        if p[l][0]=="*":
            continue
        tmp=""
        for k in range(len(p[l])):
            if p[l][k]=="*":
                tmp=tmp+p[l][k]
                break
            tmp=tmp+p[l][k]

        head_list.append(tmp)
    
    head_len=0
    long_header=""
    for header in head_list:
        if len(header)>head_len:
            head_len=len(header)
            long_header=header

    #print("head_list,long_header",head_list,long_header)]
    no_ast_flg=0
    if len(long_header)>0:
        if long_header[-1]!="*":
            no_ast_flg=1

            
    ng_flg=0
    p2=[]
    for l in range(n):
        if p[l][0]=="*":
            p2.append(p[l])
        else:
            for k in range(len(long_header)):
                if p[l][k]=="*":
                    p2.append(p[l][k:])
                    break
                if p[l][k]!=long_header[k]:
                    ng_flg=1
                    break
            if ng_flg:
                break

    #print("p2",p2)

    tail_list=[]
    for l in p2:
        if l[-1]=="*":
            continue
        tmp=""
        for k in range(len(l)-1,-1,-1):
            #print("l[l]",l[k])
            if l[k]=="*":
                tmp=l[k]+tmp
                break
            tmp=l[k]+tmp
        
        tail_list.append(tmp)

    tail_len=0
    long_tail=""
    for tail in tail_list:
        if len(tail)>tail_len:
            tail_len=len(tail)
            long_tail = tail

    #print("tail_list,ling_tail",tail_list,long_tail)

    p3=[]
    for l in range(len(p2)):
        if p2[l][-1]=="*":
            p3.append(p2[l])
        else:
            for k in range(-1,-len(long_tail)-1,-1):
                #print("k=",k,",p2 l k = ",p2[l][k],", long_tail[k]= ",long_tail[k])
                if p2[l][k]=="*":
                    p3.append(p2[l][:k+1])
                    break
                if p2[l][k]!=long_tail[k]:
                    ng_flg=1
                    break
            if ng_flg:
                break
    #print(p3,ng_flg)

    ans_tmp = long_header
    for l in p3:
        ans_tmp = ans_tmp + l
    ans_tmp = ans_tmp + long_tail

    ans=""
    for l in range(len(ans_tmp)):
        if ans_tmp[l]!="*":
            ans=ans+ans_tmp[l]

    #print("ans=",ans)
    case_num=i+1
    if ng_flg:
        ans="*"
    if no_ast_flg:
        ans=long_header
    print('Case #%d: %s' % (case_num,ans))


