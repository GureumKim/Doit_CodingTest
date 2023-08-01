## 0번
N = int(input)
li = [int(input()) for _ in range(N)]

# selection sort
l1 = li[:]
for i in range(N-1): #len(li)-1까지
    for j in range(i,N):
        if l1[i] > l1[j]:
            l1[i], l1[j] = l1[j],l1[i]
print(*l1)

# insert sort
l2 = li[:]
result = [0]*6
for i in range(N): #len(li) 까지
    result[i] = l2[i]
    for j in range(i,0,-1):
        if result[j]<result[j-1]:
            temp = result[j]
            result[j] = result[j-1]
            result[j-1] = temp
print(*result)

# bubble sort
N = int(input)
li = [int(input()) for _ in range(N)]
for i in range(N-1,0,-1): #len(arr)-1에서 1까지
    for j in range(i): 
        if li[j]>li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
for i in range(N):
    print(li[i])

## 1번
n = int(input())
num = int(input())
Sum = 0
for i in range(n):
    Sum+=num%10
    num//=10
print(Sum)

# 재귀 복습
def sum_digit(num):
    if num == 0:
        return 0
    else:
        return num%10 + sum_digit(num//10)
input()
num = int(input())
print(sum_digit(num))


## 2번

#1
n = int(input())
scores = list(map(int,input().split()))
maxx = max(scores)
print(sum(map(lambda x:x/maxx,scores))/n*100)

#2
n = int(input())
scores = list(map(int,input().split()))
print(sum(scores)/max(scores)*100/n)

