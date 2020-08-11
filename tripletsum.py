def tripletsum(array_given):
    """O(n2) solution"""
    n=len(array_given)
    if n < 3:
        return False
    elif n==3:
        return array_given if sum(array_given)==0 else False
    else:
        for i in range(n):
            for j in range(i+1,n):
                k = 0-array_given[i] - array_given[j]
                if k in array_given[j+1:]:
                    return [array_given[i],array_given[j],k]
    return False


if __name__ == '__main__':
    array = [0,-1,2,-3,1]
    print(tripletsum(array))