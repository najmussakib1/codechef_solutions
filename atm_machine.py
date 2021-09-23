# cook your dish here
for _ in range(int(input())):
    N, K = list(map(int,input().split(' ')))
    tk = list(map(int,input().split(' ')))
    ans =""
    for amount in tk:
        if amount<=K:
            ans+='1'
            K-=amount
        else:
            ans+='0'
    print(ans)