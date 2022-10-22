def max_pairwise_product_fast(a):
    index1 = 0
    for i in range(1, len(a)):
        if a[i] > a[index1]:
            index1 = i
    index2 = 0
    for j in range(1, len(a)):
        if a[j] > a[index2] and j != index1:
            index2 = j
    return a[index1] * a[index2]


n = int(input())
x = input().split()
a = []
for i in range(len(x)):
    a.append(int(x[i]))
print(max_pairwise_product_fast(a))
