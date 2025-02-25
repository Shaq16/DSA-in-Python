# 2.Bubble sort

arr=[1,5,2,4,3,7,0,9]

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr) 