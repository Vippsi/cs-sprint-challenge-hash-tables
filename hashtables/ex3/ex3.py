def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for array in arrays:
        for small_arr in array:
            if small_arr not in cache:
                cache[small_arr] = 1
            else:
                cache[small_arr] += 1

    for i in cache:
        if cache[i] == len(arrays):
            print(i, cache[i], len(arrays))
            result.append(i)
            print(result)
        else:
            continue
    return result



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10, 20)) + [1, 2, 3])
    arrays.append(list(range(20, 30)) + [1, 2, 3])
    arrays.append(list(range(30, 40)) + [1, 2, 3])

    print(intersection(arrays))
