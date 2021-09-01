n = 6

#[n-1]

arr =[1,3,2,5,6]

sum = n * (n+1)/2

actualsum=0

for i in arr:
    actualsum += i

print(sum-actualsum)



select count(empname), dept from empTable group by dept


# arr.sort()
# for i in range(n):
#     if((i < n-2)):
#         if((arr[i]+1!= arr[i+1])):
#             print(arr[i] + 1)