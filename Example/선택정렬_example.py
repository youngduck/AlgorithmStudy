array=[5,2,3,4,1,9,6,8,7,0]

for i in range(len(array)):
    min_index= i #인덱스로 찾고
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j
        array[min_index],array[i]=array[i],array[min_index] #스왑

print(array)
