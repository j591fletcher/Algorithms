#bubblesort

def bubble(arr):
    length = len(arr)
    for i in range(length):
        for j in range(0,length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                 


test = [1,9,3,2,4]
bubble(test)

for i in range(len(test)):
    print (test[i], end=" ")

