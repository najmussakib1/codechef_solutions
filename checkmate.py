# cook your dish here
# problem link---- https://www.codechef.com/DEC21C/problems/CHECKMATE/



import sys
input = sys.stdin.readline
for _ in range(int(input())):
    # xk,yk,x1,y1,x2,y2
    xk, yk = list(map(int,input().split()))
    x1, y1= list(map(int,input().split()))
    x2, y2 = list(map(int,input().split()))
    ans = "NO"
    if not (xk==1 or xk==8 or yk==1 or yk==8):
        ans = "NO"
    else:
        if xk==1:
            if (x1==2 or x2==2) and y1!=y2:
                #...
                if abs(y1-yk)>1 and abs(y2-yk)>1:
                    ans="YES"
        elif xk==8:
            if (x1==7 or x2==7) and y1!=y2:
                if abs(y1-yk)>1 and abs(y2-yk)>1:
                    ans="YES"
        if yk==1:
            if (y1==2 or y2==2) and x1!=x2:
                if abs(x1-xk)>1 and abs(x2-xk)>1:
                    ans="YES"
                
        elif yk==8:
            if (y1==7 or y2==7) and x1!=x2:
                if abs(x1-xk)>1 and abs(x2-xk)>1:
                    ans="YES"
    print(ans)
