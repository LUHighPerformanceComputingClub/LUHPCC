# A bogo-sort algorithm made to show how slow single-core can be over multi-core 
# Made by Noah Harris for HPCC

import random
import time
#from mpi4py import MPI

#Functions to do the sorting
def is_sorted(arr):
    #Checks if the array is in the right order
    for num in range(len(arr)-1):
        if arr[num]>arr[num+1]:
            #Return false if the item to the left is bigger than the item to the right
            return False
    return True

def bogoSort(arr):
    #Sort through the array
    startTime= time.time()
    counter = 0
    while not is_sorted(arr):
        #built in python method that will re-arrange the array
        random.shuffle(arr)
        if(counter >=1000000):
            if(time.time()-startTime > 120):
                print(int((time.time()-startTime)/60),"minutes have elapsed.")
            else:
                print(int(time.time()-startTime),"seconds have elapsed.")
            counter = 0
        counter +=1
    endTime = time.time()
    return arr, int(endTime - startTime) + ((endTime - startTime) % 60)


#Create a list
newList = [9,2,3,1,4,7,6,0,5,8,10,11,12,13,14,15]
print("Here is the list pre-sort:",newList)
#Create the variable to hold the sorted list and the time it takes to run
sortedList, runtime = bogoSort(newList)
print("Here is the list sorted:", sortedList)
print("It took:",int(runtime/60),"minutes", runtime % 60 ,"seconds")
