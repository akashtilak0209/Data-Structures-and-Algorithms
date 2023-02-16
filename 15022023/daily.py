# Question: https://leetcode.com/problems/add-to-array-form-of-integer/

# My Solution:(Brute Force)
def mySolution(num,k):
    integer = 0
    n = len(num)
    for i,el in enumerate(num):
        integer = integer + el*(10**(n-i-1))
    #integer + k
    integer += k
    #integer to list
    lis=[]
    for element in str(integer):
        lis.append(element)

    return list(map(int,lis))

# Optimized Solution:

# Original Solution:
def originalSolution(num,k):
    num[-1] += k
    for i in range(len(num) - 1, -1, -1):
        carry, num[i] = divmod(num[i], 10)
        if i: num[i-1] += carry
    if carry:
        num = map(int, str(carry)) + num
    return num

# def originalSolution2(num,k):
#     for i in range(len(num) - 1, -1, -1):
#         k, num[i] = divmod(num[i] + k, 10)
#     while k:
#         k, a = divmod(k, 10)
#         num = [a] + num
#     return num

if __name__ == '__main__':
    num = [1,2,0,0]
    k = 34
    print(mySolution(num, k))
    print(originalSolution(num, k))
    # print(originalSolution2(num, k))
