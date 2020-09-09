pos = -1

def binsearch(list, n):
    l=0
    u=len(list)-1

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals() ['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l=mid
            else:
                u=mid

mylist = [10, 22, 45, 66, 72, 88, 99,125]
n = 99

if binsearch(mylist, n):
    print("Found at pos:", pos+1)
else:
    print("Not found")
