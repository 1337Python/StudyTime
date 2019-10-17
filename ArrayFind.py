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



##################################################################################
#question:

#add two numbers in the array together. check if the two numbers meet the target.
#if they add up to the target value return true, if not return false.

array1 = [1,3,4,6,8]
array2 = [2,4,5,7,9]
target = 10

def sumTwoNumbers(numbers, target):
    
    for i in range(len(numbers)):
        firstval = numbers[i]
        #print(str(i) + " 1st: " + str(firstval))
        for t in range(len(numbers)):
            if t == i:
                continue #so you don't add the same value in the array together
            else:
                secondval = numbers[t]
                #print(str(t) + " 2nd: " + str(secondval))
                added = firstval + secondval
                #print("added: " + str(added))
            
            if added == target:
                return True
            else:
                continue
    return False

print(sumTwoNumbers(array1, target))
print(sumTwoNumbers(array2, target))
