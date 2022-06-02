# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s,n=input().split()
n = int(n)
# s_list= s.split("")
for item in sorted(permutations(s, n)):
    print(("".join(item)))
