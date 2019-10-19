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


#Similar to bubble sort you don't need to iterate the same range.  You can start 1 above/below the current
#value of the outer loop since comparing/adding to itself is out of bounds.
def sumTwoNumbers2(numbers, target):
    numNums = len(numbers)
    searchCount = 0
    for i in range(0, numNums):
        for j in range(i+1, numNums):
            searchCount += 1
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [True, searchCount]
    return [False, searchCount]

print('----------------')    
print(sumTwoNumbers2(array1, 10))
print(sumTwoNumbers2(array2, 10))
print(sumTwoNumbers2(array1, 16))
print(sumTwoNumbers2(array2, 16))


#Note this function assumes the numbers are sorted.  My example happens to be sorted.
#But if they were not, you would need to sort them first.  
def sumTowNumbersBinarySearch(numbers, target, min, max, searchCount):
    if (max == min):
        return [False, searchCount]
    numNums = len(numbers)
    mid = int((min + max) / 2) #Integer divison loses mantissa.  4.5 becomes 4.  5.9 becomes 5, etc.
    sum = numbers[mid] + numbers[mid + 1]
    print([min, max], 'mid index =', mid, '  sum =', numbers[mid], '+', numbers[mid+1], '=', sum)
    if sum == target:
        return [True, searchCount]
    elif (mid - min) <= 1:
        return [False, searchCount]
    elif sum < target:
        return sumTowNumbersBinarySearch(numbers, target, mid, max, searchCount + 1)
    elif sum > target:
        return sumTowNumbersBinarySearch(numbers, target, min, mid, searchCount + 1)
    
array1 = [0, 1,2,3,4,5,6,7,8,9,10,21,22,23,24,25,26,27,28,29]
print('----------------*', len(array1))    
print(sumTwoNumbers2(array1, 47)) #20 numbers, naive search is N^2 or worst case of 400 searches.
print()
#Binary search halves the search area (divides by 2) each search.  So it is logrithmic, base 2.  2^4 == 16.  2^5 == 32.  20 numbers so our worst case is 5 searches.
#I'm not entirely confident on my exit case of mid - min, I may need one for max - mid as well.
print(sumTowNumbersBinarySearch(array1, 47, 0, len(array1), 1))
print()
print(sumTowNumbersBinarySearch(array1, 20, 0, len(array1), 1))
