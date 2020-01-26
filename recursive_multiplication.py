# x= 10^(n/2)*a + b
# y= 10^(n/2)*c + d

# x*y = (10^(n/2)*a + b) x (10^(n/2)*c + d)
# x*y= 10^n x a.c + 10^n/2 x (a.d + b.c) + b.d

def rec_mul(x,y):
    n=len(x)
    if n==1:
        return int(x)*int(y)
    else:
        # spliting each number into their halfs
        a=x[0:n//2]
        b=x[n//2:n]
        c=y[0:n//2]
        d=y[n//2:n]
        l=(10**n)*rec_mul(a,c)+(10**(n/2))*(rec_mul(a,d)+rec_mul(b,c))+rec_mul(b,d)
        return l

n1=input("Enter First Number : ")
n2=input("Enter Second Number : ")
prod=rec_mul(n1,n2)
print(prod)
