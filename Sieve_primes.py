def prime(n):
    a=[1]*(n-1)
    p=2
    while p*p<	n:
        if a[p-2]==1:
            for i in range(p*p,n+1,p):
                if a[i-2]==1:
                    a[i-2]=0
            p+=1
        else:
            p+=1
    for i in range(n-1):
        if a[i]==1:print(i+2)
        
n=int(input("Enter total primes = "))
prime(n)
