#Bubble sort is the easiest way to sort an array.  It is not very efficient but worth knowing
#because when you are dealing with a small amount of items, its simplicity matters.
#It is called 'bubble' because the smallest elements bubble up towards the top.


def printArray(arr):
    for val in arr:
        print("%d, " %val, end="") # end="" is Python's odd way of NOT including a newline character for every print
    print("\n")

def bubbleSort(arr): 
    n = len(arr) 
  
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                print("i:", i, "  j: ", j)
                arr[j], arr[j+1] = arr[j+1], arr[j]
                printArray(arr)
        print("")
  
# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 
  
print ("Initial array is:") 
printArray(arr)
print("")
bubbleSort(arr) 
  
print("")
print ("Sorted array is:") 
printArray(arr)














# Extra Credit.
#If you have N items (say 10) it requires N^2 (100) operations to sort the elmenents.
#In computer science this is called having a Big O notation of N^2.  
#All that means is you are comparing every element to every other element.
#When sorting, you can instead compare every element with half of all other elements.  Then repeat.
#This results in Log(N) complexity on compares but still need the N for each element.  So
#you get N*Log(N) which is drastically faster than N^2.
