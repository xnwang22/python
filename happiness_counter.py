# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n,m = list(map(int, input().split()))
lst= list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
happiness = 0;
counter = Counter(lst)
happiness=sum([counter[n] for n in A])
happiness -= sum([counter[n] for n in B])
# for i in lst:
#     if i in A:
#         happiness += 1
#     elif i in B:
#         happiness -= 1

print(happiness)
