def solution(a):
    from collections import Counter
    counter = Counter(a)
    
    if any(count > 2 for count in counter.values()):
        return []

    array1, array2 = [], []

    for number, count in counter.items():
        if count == 2:
            array1.append(number)
            array2.append(number)
    
    for number, count in counter.items():
        if count == 1:
            if len(array1) < len(a) // 2:
                array1.append(number)
            else:
                array2.append(number)
    
    return [array1, array2]

# Example usage:
a = [1, 2, 3, 4]
print(solution(a))  # Output can be: [[2, 1, 3], [2, 3, 4]]
