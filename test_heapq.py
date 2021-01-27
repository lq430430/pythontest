# -*- coding=utf-8 -*-
"""创建堆的两种方法，分别进行堆排序
1.创建空堆，然后将List中各元素分别使用heappush放入堆中
2.直接将List转换成堆"""
import heapq

#创建堆方法1

list=[12,1,53,33,123,2,52,98]
heap=[]
#将List中各元素依次放入堆中
for item in list:
    heapq.heappush(heap,item)
#print(heap[0])  #打印出堆中最小值
print([heapq.heappop(heap) for _ in range(len(list))])  #堆排序结果，使用列表推导式打印排序结果

#创建堆方法2
list=[12,1,53,33,123,2,52,98]
heapq.heapify(list)
for _ in range(len(list)):
    print(heapq.heappop(list)) #每次弹出堆中最小值

#heapq.merge(*iterables) 用于合并多个排序后的序列成一个排序后的序列， 返回排序后的值的迭代器。
num1=[32, 3, 5, 34, 54, 23, 132]
num2 = [23, 2, 12, 656, 324, 23, 54]
num1=sorted(num1)
num2=sorted(num2)

res=heapq.merge(num1,num2)  #返回合并后的迭代器
print([i for i in res])     #将迭代器循环输出

#实现堆排序
def heapsort(iterable):
    h=[]
    for value in iterable:
        heapq.heappush(h,value)
    return [heapq.heappop(h) for i in range(len(h))]
list3=[1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(heapsort(list3))

#堆的值可以是元组类型，可以实现对带权值的元素进行排序。
heap1=[]
heapq.heappush(heap1,(5, 'write code'))
heapq.heappush(heap1,(7, 'release product'))
heapq.heappush(heap1,(1, 'write spec'))
heapq.heappush(heap1,(3, 'create tests'))
print(heapq.heappop(heap1))
print(heapsort(heap1))


#如果需要删除堆中最小元素并加入一个元素，可以使用heapq.heaprepalce() 函数
list1=[1,8,44,934,2,55,23]
heapq.heapify(list1)
heapq.heapreplace(list1,888)
print([heapq.heappop(list1) for i in range(len(list1))])

#如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数支持Key参数
list2=[1,8,44,934,2,55,23]
print(heapq.nlargest(2,list2))  #nlargest(n, iterable[, key])
print(heapq.nsmallest(1,list2))

#Key参数使用
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap=heapq.nsmallest(5,portfolio,key=lambda x:x['price']) #使用lambda匿名函数，按price字段排序
expensive=heapq.nlargest(2,portfolio,key=lambda x:x['shares']) #按shares字段排序,取最大的三个值

print(cheap)
print(expensive)