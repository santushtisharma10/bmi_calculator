from googlesearch import search

query = "bubble sort"

lis = []

for j in search(query, tld='com', num=10, stop=10, pause=2.0):
    lis.append(j)

print(lis)