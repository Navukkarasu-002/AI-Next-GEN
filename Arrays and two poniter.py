# 1. Missing element:
arr = [3, 0, 1]
n = len(arr)
total = n * (n + 1) // 2
num = sum(arr)
missing = total - num
print(missing)

# 2. Reverse an arrays:
# two pointer array (odd numbers && even numbers)
#    we will maintain the tow variable to track the diiferent position of arr that is left to right

arr = [10,50,53,22]
left =0
right = len(arr)-1
while left < right:
    arr[left],arr[right] = arr[right],arr[left]
    left +=1
    right -=1
print(arr)


# 3.rewove Element
arr = [3, 2, 2, 3, 4, 5]
val = 3

j = 0

for num in arr:
    if num != val:
        arr[j] = num
        j += 1

print(j)
print(arr[:j])



# 4. Remove Element
arr = [1, 1, 2, 2, 3, 4, 4, 5]

if len(arr) == 0:
    print([])
else:
    j = 0

    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]

    print(arr[:j + 1])


#5. Move zeros
arr = [0,2,0,3,5,0,7,0,5]
j = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[j], arr[i] = arr[i],arr[j]
        j += 1
print(arr)