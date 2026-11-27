# 1. Maximum Sum Subarray of Size K
arr = [100, 200, 300, 400]
k = 2
left = 0
sum, max_sum = 0, 0

for right in range(len(arr)):
  sum += arr[right]
  while right - left + 1 > k:
    sum -= arr[left]
    left += 1
  max_sum = max(max_sum, sum)
print(max_sum)


#Maximum Element in Every Window of Size K
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

for i in range(len(arr) - k + 1):
    max_num = arr[i]

    for j in range(i, i + k):
        if arr[j] > max_num:
            max_num = arr[j]

    print(max_num)

#