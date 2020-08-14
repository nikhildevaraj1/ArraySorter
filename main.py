array1 = [5,2,1,3,4, 15, 6, 6,8,9, 11,12, 24, 23, 12, 34]

length = len(array1)


for i in range(0,length-1):
  if array1[i] > array1[i+1]:
    array1[i], array1[i+1] = array1[i+1], array1[i]
for i in range(0,length-1):
  if array1[i] > array1[i+1]:
    array1[i], array1[i+1] = array1[i+1], array1[i]
for i in range(0,length-1):
  if array1[i] > array1[i+1]:
    array1[i], array1[i+1] = array1[i+1], array1[i]
for i in range(0,length-1):
  if array1[i] > array1[i+1]:
    array1[i], array1[i+1] = array1[i+1], array1[i]
    





print(array1)