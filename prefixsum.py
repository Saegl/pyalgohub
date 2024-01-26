arr = [3, 2, 4, 1, 5]

# init prefix array
prefix = [0]
for n in arr:
    prefix.append(prefix[-1] + n)

# usage
i = 1
j = 4
print(sum(arr[i:j]) == prefix[j] - prefix[i])


# test
for i in range(len(arr)):
    for j in range(i, len(arr)):
        assert sum(arr[i:j]) == prefix[j] - prefix[i]

