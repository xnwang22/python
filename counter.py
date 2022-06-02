# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
size_count=int(input())
sizes=list(map(int, input().split()))
customers=int(input())
shoe_counter=Counter(sizes)
i=customers
proceeding=0
while i>0:
    size, price=map(int, input().split())
    if shoe_counter[size] > 0:
        proceeding += price
        shoe_counter[size] = shoe_counter[size]-1
    i = i-1
print(proceeding)
