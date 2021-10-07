# problem link--https://www.codechef.com/problems/TYPING


right = ['j','k']
for _ in range(int(input())):
    l =[]
    for x in range(int(input())):
        l.append(input())
    as_set = list(set(l))
    times = dict()
    for w in as_set:
        lp =0
        tm = 2
        prev =''
        current =''
        
        for s in w:
            lp+=1
            if lp==1:
                if s in left:
                    prev ='left'
                else:
                    prev ='right'
            else:
                if s in left:
                    current='left'
                else:
                    current='right'
                if current == prev:
                    prev = current
                    tm+=4
                else:
                    tm += 2
                    prev = current
        times[w]=tm
    init =0
    for w in as_set:
        if l.count(w)==1:
            init+=times[w]
        else:
            ano=(l.count(w)-1)*(times[w]//2)
            cc = times[w]+ano
            init+=cc
    print(init)
