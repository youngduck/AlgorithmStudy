N=int(input())
plus_data=[]
minus_data=[]

for i in range(N):
    j=int(input())
    if j>0:
        plus_data.append(j)
    else:
        minus_data.append(j)
        
plus_data=sorted(plus_data,reverse=True)
minus_data=sorted(minus_data)


def group(arr):
    sw=0
    save=0
    result=0
    result+=arr.count(1)
    for i in range(arr.count(1)):
        arr.remove(1)
    for i in range(len(arr)):
        if sw == 0:
            if i == (len(arr)-1):
                result+=arr[i]
            save += arr[i]
            sw = 1
        else:
            result += save*arr[i]
            sw=0
            save=0
    return result

result=0
result+=group(plus_data)
result+=group(minus_data)
print(result)