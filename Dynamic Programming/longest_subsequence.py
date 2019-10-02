def lcs(l1,l2):
    if len(l1)==0 or len(l2)==0:  #if length diminishes to 0 -> stop
        return(0)
    else:
        if l1[len(l1)-1]==l2[len(l2)-1]: #if last elements matches
            return(1+lcs(l1[0:len(l1)-1],l2[0:len(l2)-1]))
        else:
            return(max(lcs(l1[0:len(l1)-1],l2[0:len(l2)]),lcs(l1[0:len(l1)],l2[0:len(l2)-1])))


n,m=map(int,input().split())

l1=input() #enter string 1
l2=input()  #enter string 2

print(lcs(l1,l2))
