#1. count frequency of each element in an array
def count_frequency(arr):
 freq = {}
 for i in arr:
   if i in freq:
     freq[i]+=1
   else:
     freq[i]=1
 for i ,count in freq.items():
    print(i,":",count)
arr = [1,1,2,2,4,3,3,5,5]
count_frequency(arr)


#2. find all repeat
def find_repeat(arr):
  freq = {}
  for i in arr:
    if i in freq:
      freq[i]+=1
    else:
      freq[i]=1
  for i in freq:
    if freq[i]>1:
      print(i)
arr = [1,1,2,2,4,3,3,5,5]
find_repeat(arr)


#3. find all non-repeat
def find_repeat(arr):
  freq = {}

  for i in arr:
    if i in freq:
      freq[i]+=1
    else:
      freq[i]=1
  for i in freq:
    if freq[i]==1:
      print(i)
arr = [1,1,2,2,4,3,3,5,5]
find_repeat(arr)


#4. find first repeat
def find_repeat(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in freq:
        if freq[i] > 1:
            print(i)
            break
arr = [1, 1, 2, 2, 4, 3, 3, 5, 5]
find_repeat(arr)


#5. find first repeat
def find_repeat(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in freq:
        if freq[i] == 1:
            print(i)
            break
arr = [1, 1, 2, 2, 4, 3, 3, 5, 5]
find_repeat(arr)

