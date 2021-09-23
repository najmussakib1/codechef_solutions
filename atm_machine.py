# problem link: https://www.codechef.com/problems/ATM2
for _ in range(int(input())):
    N, K = list(map(int,input().split(' ')))
    tk = list(map(int,input().split(' ')))
    ans =""
    for amount in tk:
        if amount<=K:
            # checking if the amount is less than the initial balance of atm machine
            ans+='1'
            K-=amount
        else:
            ans+='0'
    print(ans)
