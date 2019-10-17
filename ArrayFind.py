


def FindIt(arr, find):
    sum = 0
    for val in arr:
        sum += val
        if (sum == find):
            return [True, val]
    return [False, -1]


def OptimizedFindIt(arr, find):
    sum = 0
    for val in arr:
        sum += val
        if (sum > find):
            return [False, val]
        if (sum == find):
            return [True, val]
    return [False, -1]


arr = [1, 2, 3, 4, 5] 
result = FindIt(arr, 10) # 1 + 2 + 3 + 4 == 10.  So we see we found it at value 4.
print(result)

result = FindIt(arr, 5) #We done find it but get all the way to then end of the loop so we see a -1
print(result)

result = OptimizedFindIt(arr, 5) # Here we know by the time we hit 3 we've over shot and can never find it.
print(result)
