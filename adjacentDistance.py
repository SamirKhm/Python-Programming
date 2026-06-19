arr = [10, 11, 7, 12, 14]

def adjacentDistance(arr):
    adj = []
    for i in range(len(arr) - 1):
        adj.append(abs(arr[i] - arr[i + 1]))
    return sum(adj)

print(adjacentDistance(arr))