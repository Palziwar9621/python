num="6789"
for i in range(len(num)):
    for j in range(i+1,len(num)):
        split_num=num[:i]
        split_num2=num[j:]
        print(split_num)