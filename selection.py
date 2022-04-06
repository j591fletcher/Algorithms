#selection sort

def selection(array):
    n = len(array)

    for i in range(n):
        min = i
        for j in range(i+1, n):
            if array[min] > array[j]:
                min = j
        array[i], array[min] = array[min], array[i]


test = [9,2,3,2,5,1213,22,3,4,234234,343,23,8876,9]
sameTest = [1,1,1,1,1]
selection(test)
selection(sameTest)
for i in range(len(test)):
    print (test[i], end=" ")
print("\n")
for i in range(len(sameTest)):
    print (sameTest[i], end=" ")