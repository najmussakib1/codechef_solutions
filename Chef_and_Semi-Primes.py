from math import * 

# problem code--- CHEFPRMS ,, contest---- (codechef)  SnackDown Practice Contest: Beginner
# problem link-- https://www.codechef.com/SDPCB21/problems/CHEFPRMS

"""
algorithm:
first i will loop (from 2 to a/2) through the input  number(i am considering the num as 'a'). {loop var x}
now another number will be a-x.
now i will check if x and a-x are semi-primes or not. if both are semi primes i will print YES else i will print NO.....

"""


def SieveOfEratosthenes(n, isPrime) :
    isPrime[0], isPrime[1] = False, False
 

    for i in range(2, n + 1) :

        isPrime[i] = True
 

    for p in range(2, int(sqrt(n)) + 1) :
        if isPrime[p] == True :
 

            for i in range(p * 2, n + 1, p) :

                isPrime[i] = False 

def checksemiprime(n) :
 

    flag = 0

    isPrime = [False] * (n + 1)

    SieveOfEratosthenes(n, isPrime)

    for i in range(2, n) :

        x = int(n / i)
 

        if (isPrime[i] & isPrime[x] and

             x != i and x * i == n) :

            return True

            flag = 1

            break
 

    if not flag :
      return False

T = int(input())
for _ in range(T):
  a = int(input())
  found=False
  for x in range(2,int(a/2)+1):
    s1=x
    s2=a-x
    semis1=checksemiprime(s1)
    semis2=checksemiprime(s2)
    if semis1 and semis2:
      found=True
      break
  if found:
    print("YES")
  else:
    print("NO")
