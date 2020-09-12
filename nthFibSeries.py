def getNthFib(n):
    if n==0 or n==1:
        return 0
    if n==2:
        return 1
    return getNthFib(n-1) + getNthFib(n-2)
    
    
res = getNthFib(7)
print(res)
