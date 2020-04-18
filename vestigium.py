t=int(input())
for i in range(t):
    case_num=i+1
    n = int(input())
    in_mat = []
    for j in range(n):
        in_mat.append(list(map(int,input().split())))
    #print(in_mat)

    trace = 0
    f_low = 0
    f_col = 0
    for j in range(n):
        for k in range(n):
            if j==k:
                trace = trace + in_mat[j][k]

    for j in range(n):
        for num in range(1,n+1):
            flg = False
            for k in range(n):
                #print(num,j,k)
                if num == in_mat[j][k]:
                    flg = True
                    #print("match",num,in_mat[j][k])
                    break
            if flg==False:
                f_low+=1
                break

    for k in range(n):
        for num in range(1,n+1):
            flg = False
            for j in range(n):
                if num == in_mat[j][k]:
                    flg = True
                    break
            if flg==False:
                f_col+=1
                break

    #print("trace=",trace)
    #print("f_low=",f_low)
    #print("f_col",f_col)
    print('Case #%d: %d %d %d' % (case_num,trace,f_low,f_col))