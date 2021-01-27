#找出最大数
a=[32,11,55,23,64,23]
max=a[0]
for i in a:
    if i>max:
        max=i
print(max)

#找出最大数和次大数
a=[32,11,55,23,64,23]
max=a[0]
second_max=a[1]
if max<second_max:
    max = a[1]
    second_max = a[0]
for i in a[2:]:
    if i>max:
        second_max=max
        max=i
    elif i==max:
        second_max=i
    elif i>second_max:
        second_max=i
print(max,second_max)