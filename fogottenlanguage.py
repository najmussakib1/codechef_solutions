# problem:  https://www.codechef.com/problems/FRGTNLNG
for _ in range(int(input())):
    N,K= list(map(int,input().split(' ')))
    words = input().split(' ')
    p1=[]
    for i in range(K):
        p1.append(input().split(' ')[1::])
    phrases=[]
    for p in p1:
        for pg in p:
            phrases.append(pg)
    del p1
    yesorno =[]
    for w in words:
        if w in phrases:
            yesorno.append('YES')
        else:
            yesorno.append('NO')
    dstr = ""
    loop=0
    for yn in yesorno:
        loop+=1
        dstr+=yn
        if loop!=N:
            dstr+=" "
    print(dstr)
