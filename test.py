from functools import reduce

nums = [3, 5, 6, 7, 8,2,4, 10]

evens= list(filter(lambda a: a%2==0, nums))

print("Even numbers:",evens) 

mymap = list(map(lambda b: b*2, evens))

print("Mapped values are:", mymap)

reduce = reduce(lambda a,b: a+b, mymap)

print("redduced value:", reduce)