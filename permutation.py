# Write an algorithm for permutation of digits of a number
from typing import List
# def permutation_number(number:int)-> List[str]:
#     if not isinstance(number,int):
#         try:
#             number=int(number)
#         except ValueError:
#             return 'input is not a number'
#     else:
#         digits=list(str(number))
#         result = permute_digits(digits)
#         return result

# def permute_digits(digits:List[str])->List[str]:
#     permutations=[]
#     if len(digits) == 1:
#         return digits
#     else:
#         for j in range(len(digits)):
#             permutations.extend(digits[0] + i for i in  permute_digits(digits[1:]))
#             permutations.extend( i + digits[0] for i in  permute_digits(digits[1:]))
#             permutations.extend(i + digits[j] for i in permute_digits(digits[0:j]+ digits[j:]))
#         return permutations


# Python program to print all permutations using
# Heap's algorithm

# Prints the array
def printArr(a, n):
    for i in range(n):
        print(a[i], end=" ")
    print()


# Generating permutation using Heap Algorithm
def heapPermutation(a, size, n):
    # if size becomes 1 then prints the obtained
    # permutation
    if (size == 1):
        printArr(a, n)
        return

    for i in range(size):
        heapPermutation(a, size - 1, n);

        # if size is odd, swap first and last
        # element
        # else If size is even, swap ith and last element
        if size & 1:
            a[0], a[size - 1] = a[size - 1], a[0]
        else:
            a[i], a[size - 1] = a[size - 1], a[i]

# Driver code
a = [1, 2, 3, 4 ]
n = len(a)
heapPermutation(a, n, n)